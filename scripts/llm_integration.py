"""
Local LLM Integration Module
Integrates local LLM (Llama) for Ardupilot configuration assistance
Optimized for CPU systems with 16GB RAM
"""

import os
import json
from typing import Dict, List, Any, Optional
import warnings

warnings.filterwarnings('ignore')


class LocalLLM:
    """
    Local LLM wrapper for Ardupilot assistance
    Uses llama-cpp-python for efficient CPU inference
    """

    def __init__(self, model_path: Optional[str] = None):
        self.model_path = model_path or os.path.join(
            '/workspace/app-b6ukc6ytkow1/backend/models',
            'llama-2-7b-chat.Q4_K_M.gguf'
        )
        self.model = None
        self.context_size = 2048
        self.max_tokens = 512

    def load_model(self):
        """Load the local LLM model"""
        try:
            from llama_cpp import Llama

            print(f"Loading model from {self.model_path}...")

            # Check if model exists
            if not os.path.exists(self.model_path):
                print(f"Model not found at {self.model_path}")
                print("Please download a GGUF model (e.g., Llama-2-7B-Chat)")
                print("Recommended: https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF")
                return False

            # Load model with CPU-optimized settings
            self.model = Llama(
                model_path=self.model_path,
                n_ctx=self.context_size,
                n_threads=4,  # Adjust based on CPU cores
                n_batch=512,
                n_gpu_layers=0,  # CPU only
                verbose=False
            )

            print("Model loaded successfully!")
            return True

        except ImportError:
            print("llama-cpp-python not installed. Install with: pip install llama-cpp-python")
            return False
        except Exception as e:
            print(f"Error loading model: {e}")
            return False

    def generate_response(self, prompt: str, temperature: float = 0.7) -> str:
        """Generate response from local LLM"""
        if not self.model:
            return "Model not loaded. Please load the model first."

        try:
            response = self.model(
                prompt,
                max_tokens=self.max_tokens,
                temperature=temperature,
                top_p=0.95,
                repeat_penalty=1.1,
                stop=["</s>", "User:", "\n\n\n"]
            )

            return response['choices'][0]['text'].strip()

        except Exception as e:
            print(f"Error generating response: {e}")
            return f"Error: {str(e)}"

    def create_ardupilot_prompt(self,
                                user_query: str,
                                context: Dict[str, Any],
                                knowledge_base_info: str = "") -> str:
        """
        Create a specialized prompt for Ardupilot configuration
        """
        system_prompt = """You are an expert Ardupilot configuration assistant. 
You help users configure their aircraft by recommending appropriate hardware and parameters.
You base your recommendations strictly on the Ardupilot knowledge base provided.
Never suggest parameters or hardware that are not in the knowledge base.
Be precise, technical, and safety-conscious."""

        user_context = f"""
Aircraft Specifications:
- Model: {context.get('model', 'Unknown')}
- Weight: {context.get('weight', 'Unknown')} kg
- Wingspan: {context.get('wingspan', 'Unknown')} m
- Additional Details: {context.get('details', 'None')}

Knowledge Base Information:
{knowledge_base_info}

User Question: {user_query}

Please provide a detailed, technical response based on the knowledge base."""

        # Format for Llama-2-Chat
        prompt = f"""<s>[INST] <<SYS>>
{system_prompt}
<</SYS>>

{user_context} [/INST]"""

        return prompt

    def recommend_configuration(self,
                                aircraft_specs: Dict[str, Any],
                                knowledge_base_context: str) -> str:
        """
        Generate configuration recommendations for an aircraft
        """
        query = "Based on my aircraft specifications, recommend the complete hardware list and critical parameter settings."

        prompt = self.create_ardupilot_prompt(
            user_query=query,
            context=aircraft_specs,
            knowledge_base_info=knowledge_base_context
        )

        return self.generate_response(prompt, temperature=0.5)

    def analyze_parameters(self,
                           current_params: Dict[str, Any],
                           aircraft_specs: Dict[str, Any],
                           knowledge_base_context: str) -> str:
        """
        Analyze current parameters and suggest improvements
        """
        params_str = json.dumps(current_params, indent=2)

        query = f"""Analyze these current parameters and suggest improvements:
{params_str}

Focus on safety, performance, and best practices."""

        prompt = self.create_ardupilot_prompt(
            user_query=query,
            context=aircraft_specs,
            knowledge_base_info=knowledge_base_context
        )

        return self.generate_response(prompt, temperature=0.3)


class LLMWithFallback:
    """
    LLM system with local model and OpenAI fallback
    """

    def __init__(self, openai_api_key: Optional[str] = None):
        self.local_llm = LocalLLM()
        self.openai_api_key = openai_api_key or os.getenv('OPENAI_API_KEY')
        self.use_local = False

        # Try to load local model
        if self.local_llm.load_model():
            self.use_local = True
            print("Using local LLM")
        elif self.openai_api_key:
            print("Local LLM not available, will use OpenAI API")
        else:
            print("Warning: Neither local LLM nor OpenAI API available")

    def generate_response(self, prompt: str, temperature: float = 0.7) -> str:
        """Generate response using available LLM"""
        if self.use_local:
            return self.local_llm.generate_response(prompt, temperature)
        elif self.openai_api_key:
            return self._generate_openai_response(prompt, temperature)
        else:
            return "No LLM available. Please configure local model or OpenAI API key."

    def _generate_openai_response(self, prompt: str, temperature: float) -> str:
        """Generate response using OpenAI API"""
        try:
            from openai import OpenAI

            client = OpenAI(api_key=self.openai_api_key)

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an expert Ardupilot configuration assistant."},
                    {"role": "user", "content": prompt}
                ],
                temperature=temperature,
                max_tokens=1000
            )

            return response.choices[0].message.content

        except Exception as e:
            print(f"Error with OpenAI API: {e}")
            return f"Error generating response: {str(e)}"

    def recommend_configuration(self,
                                aircraft_specs: Dict[str, Any],
                                knowledge_base_context: str) -> str:
        """Generate configuration recommendations"""
        if self.use_local:
            return self.local_llm.recommend_configuration(aircraft_specs, knowledge_base_context)
        else:
            # Create simplified prompt for OpenAI
            prompt = f"""Based on these aircraft specifications, recommend hardware and parameters:

Aircraft: {aircraft_specs.get('model')}
Weight: {aircraft_specs.get('weight')} kg
Wingspan: {aircraft_specs.get('wingspan')} m

Knowledge Base:
{knowledge_base_context}

Provide specific hardware recommendations and critical parameter settings."""

            return self._generate_openai_response(prompt, temperature=0.5)


def main():
    """Test the LLM integration"""
    print("=== Testing LLM Integration ===\n")

    llm = LLMWithFallback()

    test_specs = {
        'model': 'Test Fixed-Wing',
        'weight': 3.5,
        'wingspan': 1.8,
        'details': 'Long-range surveillance aircraft'
    }

    test_context = """
Available Hardware:
- Pixhawk 4 Flight Controller
- Brushless Motor 2830 1000KV
- Digital Servo 20kg

Key Parameters:
- ARSPD_TYPE: Airspeed sensor type
- BATT_CAPACITY: Battery capacity in mAh
- THR_MAX: Maximum throttle percentage
"""

    print("Generating configuration recommendations...\n")
    response = llm.recommend_configuration(test_specs, test_context)
    print(response)


if __name__ == '__main__':
    main()
