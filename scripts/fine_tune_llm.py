"""
Fine-tuning Script for Local LLM
Prepares and fine-tunes a local LLM with Ardupilot knowledge base
"""

import json
import os
from typing import List, Dict, Any


class LLMFineTuner:
    """
    Prepares training data and fine-tunes local LLM with Ardupilot knowledge
    """

    def __init__(self, data_dir: str = '/workspace/app-b6ukc6ytkow1/backend/data'):
        self.data_dir = data_dir
        self.training_data = []

    def load_knowledge_base(self) -> Dict[str, Any]:
        """Load all knowledge base data"""
        knowledge = {
            'parameters': [],
            'hardware': [],
            'equipment': {}
        }

        # Load parameters
        params_file = os.path.join(self.data_dir, 'ardupilot_parameters.json')
        if os.path.exists(params_file):
            with open(params_file, 'r') as f:
                data = json.load(f)
                knowledge['parameters'] = data.get('parameters', [])

        # Load hardware
        hardware_file = os.path.join(self.data_dir, 'ardupilot_hardware.json')
        if os.path.exists(hardware_file):
            with open(hardware_file, 'r') as f:
                data = json.load(f)
                knowledge['hardware'] = data.get('hardware', [])

        # Load equipment
        equipment_file = os.path.join(self.data_dir, 'equipment_database.json')
        if os.path.exists(equipment_file):
            with open(equipment_file, 'r') as f:
                data = json.load(f)
                knowledge['equipment'] = data.get('equipment', {})

        return knowledge

    def create_training_examples_from_parameters(self, parameters: List[Dict]) -> List[Dict]:
        """Create training examples from parameters"""
        examples = []

        for param in parameters:
            # Q&A about parameter purpose
            examples.append({
                'instruction': f"What does the {param['name']} parameter do in Ardupilot?",
                'input': '',
                'output': param['description']
            })

            # Q&A about parameter values
            if param.get('values'):
                values_str = ', '.join(param['values'])
                examples.append({
                    'instruction': f"What are the possible values for {param['name']}?",
                    'input': '',
                    'output': f"The possible values are: {values_str}"
                })

            # Category-based questions
            examples.append({
                'instruction': f"What category does {param['name']} belong to?",
                'input': '',
                'output': f"{param['name']} belongs to the {param.get('category', 'General')} category."
            })

        return examples

    def create_training_examples_from_hardware(self, hardware: List[Dict]) -> List[Dict]:
        """Create training examples from hardware"""
        examples = []

        for hw in hardware:
            # Q&A about hardware
            examples.append({
                'instruction': f"Tell me about {hw['name']}",
                'input': '',
                'output': hw['description']
            })

            # Specifications
            if hw.get('specifications'):
                specs_str = json.dumps(hw['specifications'], indent=2)
                examples.append({
                    'instruction': f"What are the specifications of {hw['name']}?",
                    'input': '',
                    'output': f"Specifications:\n{specs_str}"
                })

            # Pin connections
            if hw.get('pin_connections'):
                examples.append({
                    'instruction': f"What are the pin connections for {hw['name']}?",
                    'input': '',
                    'output': json.dumps(hw['pin_connections'], indent=2)
                })

        return examples

    def create_training_examples_from_equipment(self, equipment: Dict) -> List[Dict]:
        """Create training examples from equipment database"""
        examples = []

        # Electric motors
        for motor in equipment.get('engines', {}).get('electric', []):
            examples.append({
                'instruction': f"Recommend an electric motor for a {motor.get('applications', [''])[0]}",
                'input': '',
                'output': f"I recommend the {motor['name']}. Specifications: KV rating {motor.get('kv_rating')}, Max power {motor.get('max_power')}, Weight {motor.get('weight')}. Price range: {motor.get('price_range')}"
            })

        # Gasoline engines
        for engine in equipment.get('engines', {}).get('gasoline', []):
            examples.append({
                'instruction': f"What gasoline engine is suitable for {engine.get('applications', [''])[0]}?",
                'input': '',
                'output': f"The {engine['name']} is suitable. It has {engine.get('displacement')} displacement, {engine.get('max_power')} power, and provides {engine.get('flight_time')} flight time. Price range: {engine.get('price_range')}"
            })

        # Servos
        for servo in equipment.get('servos', []):
            examples.append({
                'instruction': f"Recommend a servo for {servo.get('applications', [''])[0]}",
                'input': '',
                'output': f"I recommend the {servo['name']}. It provides {servo.get('torque')} torque with {servo.get('speed')} speed. Weight: {servo.get('weight')}. Price range: {servo.get('price_range')}"
            })

        return examples

    def create_configuration_examples(self) -> List[Dict]:
        """Create examples for aircraft configuration scenarios"""
        examples = [
            {
                'instruction': 'Recommend hardware for a small fixed-wing aircraft weighing 2kg with 1.2m wingspan',
                'input': '',
                'output': '''For a small fixed-wing aircraft (2kg, 1.2m wingspan), I recommend:

Flight Controller: Pixhawk 4 or similar
Motor: Brushless Outrunner 2212 920KV (200W, suitable for 10x4.5 prop)
ESC: 30A Brushless ESC with BEC
Servos: 4x Standard 9g servos for control surfaces
Battery: 3S or 4S LiPo, 2200-3300mAh
Telemetry: HolyBro SiK Telemetry Radio (433MHz/915MHz)

Critical Parameters:
- ARSPD_TYPE: Set based on airspeed sensor
- BATT_CAPACITY: Set to your battery mAh
- THR_MAX: Start at 75%, adjust based on testing
- SERVO1-4_FUNCTION: Assign to aileron, elevator, throttle, rudder'''
            },
            {
                'instruction': 'What parameters should I check for a new aircraft setup?',
                'input': '',
                'output': '''For a new aircraft setup, check these critical parameters:

1. RC Input (RC1-RC16): Verify all channels are mapped correctly
2. SERVO outputs (SERVO1-16_FUNCTION): Assign control surfaces
3. ARSPD_TYPE: Configure airspeed sensor
4. BATT_CAPACITY and BATT_MONITOR: Battery monitoring
5. THR_MIN, THR_MAX, THR_CRUISE: Throttle settings
6. TRIM_ARSPD_CM: Cruise airspeed
7. RTL_ALTITUDE: Return-to-launch altitude
8. FENCE settings: Geofence for safety

Always test on the ground before flight!'''
            },
            {
                'instruction': 'How do I calculate flight range for my aircraft?',
                'input': '',
                'output': '''Flight range calculation depends on:

For Electric Aircraft:
- Battery capacity (mAh) and voltage
- Motor efficiency and current draw
- Aircraft weight and drag
- Cruise speed
Formula: Range ≈ (Battery_Wh / Power_W) × Speed_m/s

For Gasoline Aircraft:
- Fuel tank capacity
- Engine fuel consumption (ml/hour)
- Cruise speed
Formula: Range ≈ (Fuel_ml / Consumption_ml/h) × Speed_m/s

Add 20-30% safety margin. Monitor battery/fuel in real-time during flight.'''
            }
        ]

        return examples

    def generate_training_dataset(self) -> List[Dict]:
        """Generate complete training dataset"""
        print("Loading knowledge base...")
        knowledge = self.load_knowledge_base()

        print("Creating training examples...")
        training_data = []

        # Add parameter examples
        if knowledge['parameters']:
            param_examples = self.create_training_examples_from_parameters(knowledge['parameters'])
            training_data.extend(param_examples)
            print(f"Created {len(param_examples)} parameter examples")

        # Add hardware examples
        if knowledge['hardware']:
            hardware_examples = self.create_training_examples_from_hardware(knowledge['hardware'])
            training_data.extend(hardware_examples)
            print(f"Created {len(hardware_examples)} hardware examples")

        # Add equipment examples
        if knowledge['equipment']:
            equipment_examples = self.create_training_examples_from_equipment(knowledge['equipment'])
            training_data.extend(equipment_examples)
            print(f"Created {len(equipment_examples)} equipment examples")

        # Add configuration examples
        config_examples = self.create_configuration_examples()
        training_data.extend(config_examples)
        print(f"Created {len(config_examples)} configuration examples")

        print(f"\nTotal training examples: {len(training_data)}")
        return training_data

    def save_training_data(self, output_file: str = 'training_data.json'):
        """Save training data in format suitable for fine-tuning"""
        training_data = self.generate_training_dataset()

        output_path = os.path.join(self.data_dir, output_file)

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(training_data, f, indent=2, ensure_ascii=False)

        print(f"\nTraining data saved to {output_path}")

        # Also save in Alpaca format for compatibility
        alpaca_format = []
        for example in training_data:
            alpaca_format.append({
                'instruction': example['instruction'],
                'input': example.get('input', ''),
                'output': example['output']
            })

        alpaca_path = os.path.join(self.data_dir, 'training_data_alpaca.json')
        with open(alpaca_path, 'w', encoding='utf-8') as f:
            json.dump(alpaca_format, f, indent=2, ensure_ascii=False)

        print(f"Alpaca format saved to {alpaca_path}")

    def create_fine_tuning_instructions(self):
        """Create instructions for fine-tuning the model"""
        instructions = """
# Fine-Tuning Instructions for Ardupilot LLM

## Prerequisites
1. Install required packages:
   ```bash
   pip install torch transformers datasets peft bitsandbytes accelerate
   ```

2. Download base model (Llama-2-7B or similar):
   - Llama-2-7B-Chat: https://huggingface.co/meta-llama/Llama-2-7b-chat-hf
   - Or use GGUF format: https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF

## Fine-Tuning with LoRA (Recommended for 16GB RAM)

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from datasets import load_dataset
import torch

# Load model in 4-bit for memory efficiency
model_name = "meta-llama/Llama-2-7b-chat-hf"
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    load_in_4bit=True,
    device_map="auto",
    torch_dtype=torch.float16
)

tokenizer = AutoTokenizer.from_pretrained(model_name)

# Prepare model for training
model = prepare_model_for_kbit_training(model)

# LoRA configuration
lora_config = LoraConfig(
    r=16,
    lora_alpha=32,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)

model = get_peft_model(model, lora_config)

# Load training data
dataset = load_dataset('json', data_files='training_data_alpaca.json')

# Training arguments
training_args = TrainingArguments(
    output_dir="./ardupilot-llm-finetuned",
    num_train_epochs=3,
    per_device_train_batch_size=4,
    gradient_accumulation_steps=4,
    learning_rate=2e-4,
    fp16=True,
    save_steps=100,
    logging_steps=10
)

# Train model
# ... (use Trainer from transformers)
```

## Converting to GGUF for CPU Inference

After fine-tuning, convert to GGUF format for efficient CPU inference:

```bash
# Install llama.cpp
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
make

# Convert model
python convert.py /path/to/finetuned/model --outfile ardupilot-llm.gguf --outtype q4_K_M
```

## Using the Fine-Tuned Model

Place the GGUF file in: `/workspace/app-b6ukc6ytkow1/backend/models/`

The LLM integration module will automatically load it.

## Notes
- Fine-tuning on CPU is very slow. Use Google Colab with GPU if possible.
- LoRA fine-tuning requires ~12GB RAM with 4-bit quantization
- Full fine-tuning requires 40GB+ RAM (not recommended)
- For 16GB RAM systems, use pre-quantized models and LoRA
"""

        instructions_path = '/workspace/app-b6ukc6ytkow1/backend/FINE_TUNING_INSTRUCTIONS.md'
        with open(instructions_path, 'w') as f:
            f.write(instructions)

        print(f"\nFine-tuning instructions saved to {instructions_path}")


def main():
    """Generate training data and instructions"""
    print("=== Ardupilot LLM Fine-Tuning Data Generator ===\n")

    fine_tuner = LLMFineTuner()

    # Generate and save training data
    fine_tuner.save_training_data()

    # Create fine-tuning instructions
    fine_tuner.create_fine_tuning_instructions()

    print("\n=== Complete! ===")
    print("Next steps:")
    print("1. Review training_data.json and training_data_alpaca.json")
    print("2. Follow instructions in FINE_TUNING_INSTRUCTIONS.md")
    print("3. Place fine-tuned GGUF model in backend/models/")


if __name__ == '__main__':
    main()
