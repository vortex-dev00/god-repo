# 🤖 Robotics & Embodied AI

> Humanoid robots, autonomous systems, vision-language-action models, ROS, and physical AI.

---

## 1. CURRENT LANDSCAPE (June 2026)

Embodied AI is experiencing its "ChatGPT moment" — Foundation models are being connected to physical actuators. Vision-Language-Action (VLA) models allow robots to understand natural language commands and execute physical tasks. Companies like Tesla, Figure, and 1X are shipping (or near-shipping) general-purpose humanoid robots.

---

## 2. HUMANOID ROBOTS

| Robot | Company | Status (2026) | Key Features | Link |
|-------|---------|---------------|-------------|------|
| **Optimus (Gen 3)** | Tesla | Pilot production, factory deployment | Bipedal, dexterous hands, trained via human teleoperation + RL, targets <$20K eventual cost | https://tesla.com/optimus [?] |
| **Figure 01 / 02** | Figure AI | Commercial pilots, BMW factory | Partnership with OpenAI for language+vision. 5-DoF hands. Walking + manipulation. | https://figure.ai/ |
| **Atlas (Electric)** | Boston Dynamics | R&D / Commercial pilots | Most athletic humanoid. Full-body manipulation. Electric (retired hydraulic). | https://bostondynamics.com/atlas/ |
| **NEO** | 1X Technologies | Limited commercial | Bipedal, trained on neural networks, safety-focused design | https://1x.tech/ |
| **Digit** | Agility Robotics | Warehouse deployment | Purpose-built for logistics, working in Amazon facilities | https://agilityrobotics.com/ |
| **Phoenix / GR-2** | Sanctuary AI / Fourier | R&D | Carbon (Sanctuary) — "world's first robot mind" trained on general manipulation | https://sanctuary.ai/ |
| **Unitree H1/G1** | Unitree | Commercial | Chinese humanoid, aggressive pricing (~$16K for G1), open-ish ecosystem | https://unitree.com/ |
| **CL-1** | LimX Dynamics | R&D | Chinese, full-size humanoid, stair climbing | https://limxdynamics.com/ [?] |

---

## 3. ROBOT DOGS & QUADRUPEDS

| Robot | Company | Use Case | Link |
|-------|---------|----------|------|
| **Spot** | Boston Dynamics | Industrial inspection, security, construction | https://bostondynamics.com/spot/ |
| **Go2 / B2** | Unitree | Consumer/research robot dog (~$1,600 for Go2) | https://unitree.com/ |
| **ANYmal** | ANYbotics | Industrial inspection (oil/gas, mining) | https://anybotics.com/ |
| **MIT Mini Cheetah** | MIT | Research platform (open-source controller) | https://github.com/mit-biomimetics [?] |

---

## 4. VISION-LANGUAGE-ACTION (VLA) MODELS

The key breakthrough: models that take vision + language input and output physical actions.

| Model | Lab | Architecture | Key Contribution | Link |
|-------|-----|-------------|-----------------|------|
| **RT-2** | Google DeepMind | PaLM-E + Robotics Transformer | First large VLM directly controlling robots | https://arxiv.org/abs/2307.15818 |
| **RT-X (Open X-Embodiment)** | Google + 33 labs | Cross-embodiment dataset + model | Trained across 22 robot types, transfers between them | https://robotics-transformer-x.github.io/ |
| **Octo** | UC Berkeley | Diffusion policy + transformer | Open-source, generalizable manipulation policy | https://github.com/octo-models/octo |
| **OpenVLA** | Stanford/Berkeley | Fine-tuned Llama 7B as VLA | Open-source VLA — vision in, actions out. ⭐ 2,000+ | https://github.com/openvla/openvla |
| **π₀ (Pi-Zero)** | Physical Intelligence (π) | Flow-matching VLA | Generalist robot policy, multi-task, multi-robot | https://physicalintelligence.company/ |
| **GR00T** | NVIDIA | Foundation model for humanoids | Multimodal (language, video, demonstration) to robot actions | https://developer.nvidia.com/project-gr00t [?] |
| **Genie 2** | Google DeepMind | World model | Generates interactive 3D environments from descriptions | https://deepmind.google/discover/blog/genie-2-a-large-scale-foundation-world-model/ |
| **UniSim** | Google | Universal simulator | Simulates real-world interactions for robot training | https://universal-simulator.github.io/unisim/ |

---

## 5. SIMULATION & TRAINING ENVIRONMENTS

| Platform | Purpose | Link |
|----------|---------|------|
| **NVIDIA Isaac Sim** | Physics-accurate robot simulation (USD-based). GPU-accelerated RL training. | https://developer.nvidia.com/isaac-sim |
| **NVIDIA Isaac Lab** | Robot learning framework built on Isaac Sim | https://github.com/isaac-sim/IsaacLab |
| **MuJoCo** (DeepMind) | Fast physics simulator, standard for RL research. Open-source since 2022. | https://github.com/google-deepmind/mujoco |
| **PyBullet** | Open-source physics simulation for robotics | https://github.com/bulletphysics/bullet3 |
| **Gazebo** | ROS-integrated simulation | https://gazebosim.org/ |
| **Genesis** | Generative physics simulation platform | https://github.com/Genesis-Embodied-AI/Genesis [?] |
| **Habitat** (Meta) | Embodied AI simulation (navigation, manipulation) | https://github.com/facebookresearch/habitat-sim |
| **SAPIEN** | Manipulation simulation with articulated objects | https://github.com/haosulab/SAPIEN [?] |
| **RoboCasa** (UT Austin) | Large-scale simulation for household robots | https://github.com/robocasa/robocasa [?] |

---

## 6. ROS (Robot Operating System)

| Component | Description | Link |
|-----------|-------------|------|
| **ROS 2 (Jazzy/Rolling)** | The standard middleware for robotics. Pub/sub, services, actions, DDS transport. | https://docs.ros.org/ |
| **MoveIt 2** | Motion planning framework for manipulation | https://moveit.ros.org/ |
| **Nav2** | Navigation stack (SLAM, path planning, obstacle avoidance) | https://docs.nav2.org/ |
| **micro-ROS** | ROS 2 for microcontrollers | https://micro.ros.org/ |
| **ROS 2 + Isaac** | NVIDIA Isaac ROS packages (GPU-accelerated perception) | https://github.com/NVIDIA-ISAAC-ROS |
| **Foxglove** | Web-based robotics observability/visualization | https://foxglove.dev/ |
| **PlotJuggler** | Time-series data visualization for ROS | https://github.com/facontidavide/PlotJuggler |

---

## 7. MANIPULATION & GRASPING

| Tool / Model | Description | Link |
|-------------|-------------|------|
| **Dex-Net** (UC Berkeley) | Deep learning grasp planning | https://berkeleyautomation.github.io/dex-net/ |
| **Contact-GraspNet** | 6-DoF grasp generation from point clouds | https://github.com/NVlabs/contact_graspnet |
| **AnyGrasp** | Foundation model for grasping (Graspness) | https://github.com/graspnet/anygrasp_sdk |
| **DexGraspNet** | Large-scale dataset for dexterous grasping | https://github.com/PKU-EPIC/DexGraspNet [?] |
| **ALOHA** (Stanford/Google) | Low-cost bimanual teleoperation hardware for data collection | https://github.com/tonyzhaozh/aloha |
| **UMI (Universal Manipulation Interface)** | Cheap data collection with a GoPro on a gripper | https://umi-gripper.github.io/ [?] |

---

## 8. AUTONOMOUS VEHICLES & DRONES

| Platform | Type | Link |
|----------|------|------|
| **Waymo** | L4 autonomous driving (operational in SF, Phoenix, LA) | https://waymo.com/ |
| **Tesla FSD** | L2+/L3 autonomous driving | https://tesla.com/autopilot |
| **Autoware** | Open-source autonomous driving stack | https://github.com/autowarefoundation/autoware |
| **CARLA** | Open-source driving simulator | https://github.com/carla-simulator/carla |
| **PX4** | Open-source drone autopilot | https://github.com/PX4/PX4-Autopilot |
| **ArduPilot** | Open-source vehicle autopilot (drones, rovers, boats) | https://github.com/ArduPilot/ardupilot |
| **AirSim** (Microsoft) | Drone/car simulation with RL support | https://github.com/microsoft/AirSim |

---

## 9. KEY RESEARCH LABS

| Lab | Affiliation | Focus | Link |
|-----|------------|-------|------|
| **Physical Intelligence (π)** | Startup ($400M+) | General-purpose robot foundation models | https://physicalintelligence.company/ |
| **Google DeepMind Robotics** | Google | RT-X, VLA models, Gemini for robots | https://deepmind.google/discover/blog/ |
| **Tesla AI / Optimus** | Tesla | Humanoid robots at scale | https://tesla.com/optimus |
| **NVIDIA Robotics** | NVIDIA | Isaac, GR00T, simulation at scale | https://developer.nvidia.com/robotics |
| **Stanford IRIS Lab** | Stanford | Mobile ALOHA, diffusion policies, VLAs | https://irislab.stanford.edu/ [?] |
| **Berkeley AUTOLAB / BAIR** | UC Berkeley | Octo, Dex-Net, manipulation | https://autolab.berkeley.edu/ |
| **MIT CSAIL** | MIT | Soft robotics, learning for control | https://www.csail.mit.edu/ |
| **CMU Robotics Institute** | CMU | Legged locomotion, manipulation | https://www.ri.cmu.edu/ |

---

## 10. GETTING STARTED

### If you want to learn robotics + AI:
1. **Start with simulation:** MuJoCo or Isaac Sim
2. **Learn ROS 2:** https://docs.ros.org/en/jazzy/Tutorials.html
3. **Try manipulation:** ALOHA or Octo in simulation
4. **Papers to read:** RT-2, OpenVLA, Diffusion Policy

### If you want hardware:
- **Budget:** Unitree Go2 ($1,600) + Jetson Orin
- **Research:** ALOHA hardware (~$20K for bimanual setup)
- **Serious:** Franka Emika Panda / Universal Robots UR5

---

*Last updated: June 2026. [?] = unverified.*
