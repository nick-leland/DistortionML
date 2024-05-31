# MazeSolverML
Summer of Shipping project to incorporate machine learning capabilities to solve mazes by learning maze generating patterns.

# Project: Interactive AI Maze Solver

## 1. Maze Generation Algorithm
- **Basic Maze Aspects**
  - Walls
  - Start Point
  - End Point
- Seed Capabilities
- **Multiple Layouts**?
- **Generation Limitations**:
  - Need to define the constraints for maze generation
- **Target Language**
  - Python for Demo and initial design
  - Rust / C++ for Deployment and optimization 
- **Test Cases**
  - Utilize the seeding system to establish defined test cases

## 2. Machine Learning Model
- **Generation Algorithm**: 
  - **Generates data with solutions**
  - **Generates Data Without Solutions**
- **Languages**: Python/Jax

## 3. User-Generated Mazes
- **Program to Allow Users to Create Mazes**:
  - Should be deployable but think about this later on
    - Maybe use something scaleable like Spark?
- **Users need some way to be able to create their own mazes**
  - The easier it is to accomplish this the better, more creativity is beneficial I believe
- **Using Image Recognition**:
  - Use MS Paint for image recognition to construct a maze?
  - Maybe a direct GPT pipeline?
- **Database Creation**:
  - Create a database of "User Generated Mazes"

## 4. Model Fine-Tuning
- **Statement**:
  - Most people are not maze generation algorithms (Inception analogy: maze that takes X time to solve)
- **Objective**:
  - Model identifies common "human" input mazes and solves them blindly as a case (comparable to a policy algorithm)
- **Fine-Tuning Process**:
  - Fine-tune model on user-generated mazes

## 5. Visualization and Deployment
- **Visualization**:
  - Visualization to run on deployment (e.g., Think Turtles "racing" the maze)
- **Demo/Testing**:
  - Languages: Python, Rust, C++
  - Deployment considerations
- **Test Cases**:
  - Seed a classic test case opportunity

## 6. Research Points
- **Maze Generation**:
  - Study various maze generation techniques
- **Pathfinding Algorithms**:
  - Explore different algorithms for solving mazes
- **Rust**:
  - Consider using Rust for performance-critical parts
- **Deployability**:
  - Plan for how to deploy the solution
  - Maybe use Apache Spark to get experience in larger deployments
- **Jax/PyTorch**:
  - Use these frameworks for machine learning model training

---

# Action Items
1. **Maze Generation**:
   - Develop and implement algorithms with specified capabilities and limitations.
2. **Data Collection**:
   - Gather user-generated mazes and create a database.
3. **Model Training**:
   - Train and fine-tune the model using both generated and user-provided mazes.
4. **Deployment**:
   - Plan and execute the deployment of the model and visualization tools.
5. **Research and Development**:
   - Continue research on maze generation, pathfinding algorithms, and deployability.

# Current Problems
- How do we define a _move_ in the maze?

