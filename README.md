# Windows BrainLinkDualSDK Guide

**Function：**

This document will guide third-party developers on how to parse data from BrainLink Dual devices. The current demo only supports the Windows operating system for 32-bit programs. 

**Hardware：**
   - BrainLinkDual
   - Windows PC with Bluetooth

**.NET Standard version**

- .NET Standard 2.0

## BrainLinkDualSDK_Windows Reference

- Reference the project to BrainLinkDualParser.dll with the namespace BrainLinkDual.
- Place the G2G_GS5001_serial_Lib.dll, ucrtbased.dll, and vcruntime140d.dll in the root directory of the executable file.

## Class

**BrainLinkDualParser**

### Method

**void ParseByte(byte)**: Pass in the data.

### Event

**mOnSignCallBack(int sign, int battery)**

```
sign: 0-100, where 0 indicates not worn, and 100 indicates properly worn. The battery is not in use for now.
```

**mOnRawDataCallBack(int leftRaw, int rightRaw)**

```
leftRaw: Raw EEG data from the left channel.
rightRaw: Raw EEG data from the right channel.
```

**mOnFrequencyCallBack(double[] leftFrequency, double[] rightFrequency)**

```
leftFrequency: An array with a length of 140, representing the values of the left channel's brainwave frequencies from 0 to 70 Hz.
rightFrequency: An array with a length of 140, representing the values of the right channel's brainwave frequencies from 0 to 70 Hz.
```

**mOnEEGEventCallBack(float[] leftEEG, float[] rightEEG)**

```

leftEEG: An array with a length of 10, representing the values of the brainwave signals from the left channel.
rightEEG: An array with a length of 10, representing the values of the brainwave signals from the right channel.

- Delta (0.5-4 Hz): Slow-moving brainwaves that appear as flat lines on an electroencephalogram (EEG), often present during deep sleep. Delta waves can be easily interfered with by muscle electricity caused by blinking, turning the head, or frowning when the user is awake. If the Delta wave value is high, users should try to remain still before collecting data again.
- Theta (4-8 Hz): Associated with light sleep or a drowsy, half-awake state, and also appears during deep relaxation in meditation.
- Alpha (8-13 Hz): A state of deep relaxation while awake. The brain operates more smoothly, which is the optimal state for thinking and learning.
- SMR (12-15 Hz): SMR waves, also known as Sensorimotor Rhythm, were discovered by Dr. M.B. Sterman at California State University in San Francisco. They are found in the sensory and motor cortices of the cerebral cortex. SMR waves are closely related to the brain's state of arousal and serve as a measure of brain alertness. An increase in SMR waves is associated with improved attention and cognitive function. For instance, certain neurofeedback training techniques aim to increase the strength of SMR waves to help alleviate symptoms in individuals with Attention Deficit Hyperactivity Disorder (ADHD).
- Beta (15-30 Hz): Includes MidBeta and HighBeta.
- MidBeta (15-20 Hz): A state of focused attention where the mind begins to concentrate on a single object, and the brain's oxygen consumption also increases.
- HighBeta (20-30 Hz): A state of high concentration, alertness, or mental tension.
- Gamma (30-50 Hz): Involves higher processing tasks and cognitive functions. It is very important for learning, memory, and information processing. It also accompanies extreme emotions, such as joy, excitement, or deep depression.
- Total: The sum of all brainwave values.
- Max: The maximum brainwave value.
```

**mOnBrainEventCallBack(int leftAttention, int rightAttention, int leftMeditation, int rightMeditation)**

```
leftAttention: Attention level of the left channel
rightAttention: Attention level of the right channel
leftMeditation: Relaxation level of the left channel
rightMeditation: Relaxation level of the right channel
```
# FAQ

## 1.Don't know which COM port to choose for connection in Windows system?

### video tutorial in this url https://youtu.be/ENkKVI4Av3k
After the computer's Bluetooth searches for the BrainLink Bluetooth device, pair it. The Bluetooth interface of the computer may display two BrainLink Pro device names. When pairing, please select the one with the headphone pattern in front of the device name.The computer will generate two virtual Bluetooth COM ports. When opening TouchDesigner, you don't know which COM port to choose for connection?

The correct answer is to select the output COM port for connection. So, how can you distinguish which COM port is for input and which is for output? You can go to the computer's Bluetooth settings interface, select more Bluetooth options, and then click on the COM port to see which one is the output port.

After the computer's Bluetooth locates the BrainLink Bluetooth device, proceed with the pairing. The computer will create two virtual Bluetooth COM ports. When you open TouchDesigner, you might be unsure which COM port to select for the connection.

The correct approach is to choose the output COM port for the connection. How can you identify which COM port is for input and which is for output? Navigate to your computer's Bluetooth settings, select additional Bluetooth options, and then click on the COM ports to see which one is designated as the output port.
