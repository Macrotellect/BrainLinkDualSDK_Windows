# Windows BrainLinkDualSDK 开发指南

**功能：**

解析双通道脑波数据，只支持32位程序 

**支持的硬件设备：**
   - BrainLinkDual

**支持的.NET Standard**

- .NET Standard 2.0

## BrainLinkDualSDK_Windows使用参考

- 项目引用 BrainLinkDualParser.dll namespace BrainLinkDual
- 把G2G_GS5001_serial_Lib.dll ucrtbased.dll vcruntime140d.dll放到可执行文件根目录下

## Class

**BrainLinkDualParser**

### Method

**void ParseByte(byte)** 传入数据

### Event

**mOnSignCallBack(int sign, int battery)**

```
sign:0-100，0为未佩戴，100为佩戴好。battery暂未使用
```

**mOnRawDataCallBack(int leftRaw, int rightRaw)**

```
leftRaw:左通道原始脑波
rightRaw:右通道原始脑波
```

**mOnFrequencyCallBack(double[] leftFrequency, double[] rightFrequency)**

```
leftRrequency: 数组长度为140，代表左通道脑波频率0-70hz的数值
rightRrequency: 数组长度为140，代表右通道脑波频率0-70hz的数值
```

**mOnEEGEventCallBack(float[] leftEEG, float[] rightEEG)**

```

leftEEG: 数组长度为10，代表左通道脑波数值
rightEEG: 数组长度为10，代表右通道脑波数值

- Delta（0.5-4 Hz）：活动较缓慢的脑波，其在脑电图上的形状则是平缓的曲线，往往在深度睡眠时出现。德尔塔波在用户清醒状态下, 容易受到眨眼、转头、皱眉所产生的肌肉电干扰. 如德尔塔波数值较高, 请用户尽量保持静止再采集数据
- Theta（4-8 Hz）：浅度睡眠或半醒觉状态，在冥想中深度放松时也会出现 Theta 脑波
- Alpha（8-13 Hz）：醒觉状态下的深度放松状态。大脑运作较为畅顺，是思考和学习最佳状态
- SMR（12-15 Hz）： SMR 波，也称为传感器摩斯节律（Sensorimotor Rhythm），是由位于美国旧金山的加利福尼亚州立大学的 M.B. Sterman 博士发现的。它在大脑皮层中的感觉皮层和运动皮层被发现。SMR 波与大脑的觉醒状态密切相关，是衡量大脑觉醒程度的一个尺度。SMR 波的增强与提高注意力和认知功能有关。例如，某些神经反馈训练技术会尝试增加 SMR 波的强度，以帮助改善注意力缺陷障碍（ADHD）患者的症状
- Beta (15-30hz) : MidBeta和HighBeta
- MidBeta（15-20 Hz）：大脑较为专注的状态，精神开始集中于一项事物，同时大脑的血氧耗能也会加快
- HighBeta（20-30 Hz）：专注力高度集中，警觉或精神紧张的状态
- Gamma（30-50 Hz）：涉及较高的处理任务以及认知功能。对学习，记忆和信息处
理非常重要。同时伴随极端的情绪出现，例如喜乐、亢奋或极度沮丧等
- Total 脑波数值之和
- Max 脑波数值最大值

```

**mOnBrainEventCallBack(int leftAttention, int rightAttention, int leftMeditation, int rightMeditation)**

```
leftAttention: 左通道专注度
rightAttention: 右通道专注度
leftMeditation: 左通道放松度
rightMeditation: 右通道专注度
```
