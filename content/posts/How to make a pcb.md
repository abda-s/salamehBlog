---
title: How to make a pcb
description: 
date: 2024-12-25
tags: 
draft: "true"
---

## Getting Started with PCB Design and Image Editing

To begin, you'll need a basic understanding of electronics and some image editing skills. Here's what you'll need:

### Downloads

1. **[KiCad](https://www.kicad.org/)**: Used for designing the PCB.
2. **[Inkscape](https://inkscape.org/)**: Used for processing the PCB design to make it compatible with CNC software.

Additionally, you can use **Photoshop** for advanced editing, but I’ll be using **[Photopea](https://www.photopea.com/)** a free, browser-based Photoshop alternative.

---

### Drawing the Schematic

Our schematic is simple, so we'll sketch it by hand first:

**Schematic Diagram:**

![Image Description](/images/Pasted%20image%2020241226024552.png)

**Pin Details:**

- **M+, M-**: Motor pins.
- **5V**: Positive 5 volts.
- **GND**: Ground connection.
- **PWM**: Signal from the Arduino.

**Circuit Functionality:**

- This circuit controls motor speed using a PWM signal.
- The **transistor** switches the motor's power source.
- The **diode** protects the circuit from back EMF (electromotive force).
- The **resistor** ensures that the base of the transistor receives the correct voltage to operate within its safe limits, avoiding damage to the transistor.
- The **NPN transistor** allows the Arduino to provide a positive signal directly.

---

### Basics of KiCad

After installing KiCad, open the software. You should see the following interface:

![Image Description](/images/Pasted%20image%2020241226025807.png)

#### Creating a New Project in KiCad

1. Navigate to **File > New Project** or click the **New Project** icon in the toolbar.
    
    ![Image Description](/images/Pasted%20image%2020241226025931.png)
    
2. Select the location where you want to save your project and provide a name for it. Once you save, the following screen will appear:
    
    ![Image Description](/images/Pasted%20image%2020241226081252.png)
    

##### Understanding the New Files

After creating the project, two important files will be generated:

- **.kicad_sch**: This file contains the schematic diagram of the project.
    
- **.kicad_pcb**: This file contains the PCB layout of the project.
    
    ![Image Description](/images/Pasted%20image%2020241226081419.png)
    

We’ll begin by working on the schematic. Once it is completed, we’ll move on to the PCB layout.

---

#### Starting with the Schematic

1. Open the **.kicad_sch** file by double-clicking it. This will open the schematic editor, and the following screen will appear:
    
    ![Image Description](/images/Pasted%20image%2020241226083410.png)
    

##### Overview of the Schematic Editor Interface

1. **Toolbar (Box 1)**
    
    - Provides shortcuts for common actions such as creating, saving, undoing/redoing, zooming, and running the electrical rules check (ERC).
    - Also allows you to switch between different editors (e.g., schematic, PCB, symbol, and footprint editors).
2. **Tools Panel (Box 2)**
    
    - Includes tools for placing components, wires, labels, power symbols, and other elements needed to create your schematic.
    - Contains additional features for managing schematic design, such as creating connections, adding text annotations, or drawing shapes.

Now, you’re ready to start building your schematic! Let’s dive in.

we need to know how the controls work 
#### Mouse Controls

- **Left Click**:  
    Selects components, wires, or other elements.  
    If used on an empty space, it deselects the current selection.
    
- **Right Click**:  
    Opens a context menu with options relevant to the selected item or area.
    
- **Scroll Wheel**:  
    Zooms in and out of the canvas.  
    Hold the scroll wheel and move the mouse to pan around the canvas.



now click on this icon to add the components 
![Image Description](/images/Pasted%20image%2020241226084528.png)

it will give you this after loading for a sec 
![Image Description](/images/Pasted%20image%2020241226084706.png)
in the search field type thew name of the components now lets add a resistor 
type in the search feild **R** and the resistor will appear ![Image Description](/images/Pasted%20image%2020241226084855.png)
press on the result and after that OK and place the resistor on the canvas 

now lets add another component witch is the diode with the same steps 

ok now lets add the 2n2222 transistor 
we have a problem when we searched for it we didn't find any thing in KiCad 

now lets learn how to add a new component to our library in KiCad 

lets open [snap EDA](https://www.snapeda.com) and search for the name of the component 
![Image Description](/images/Pasted%20image%2020241226092718.png)
now select the result that matches the look of your component 

now this is the page after you select the component 
![Image Description](/images/Pasted%20image%2020241226092920.png)
we have two things the Symbol we will use in the schematic and the footprint we will use in the pcb layout and the two of them have different ways to import them so lets import the symbol firstly 
lets download the symbol and the footprint after we click the **Download Symbol and Footprint** button this will appear 
![Image Description](/images/Pasted%20image%2020241226101900.png)
select KiCad 

- **Note** it will ask you to log in create an account or login and continue 

now select the  version 
![Image Description](/images/Pasted%20image%2020241226103113.png)
I selected V6 & Later because my version 