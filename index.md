---
layout: default
---

# Abstract
Adversarial waveform generation has been a popular approach as the backend of singing voice conversion (SVC) to generate high-quality singing audio efficiently. However, the instability of GAN models also leads to some problems, such as pitch jitters and U/V errors. It affects the smoothness and continuity of the harmonic component, hence degrades the conversion quality seriously. To tackle this problem, this paper proposes an approach based on harmonic signals to enhance the audio generation in SVC. It firstly extracts the sine excitation from F0, then filters it with an estimated linear time-vary (LTV) filter, finally feeds both of them to the waveform generation module. Two mainstream models, MelGAN and ParallelWaveGAN, are used in the experiment to validate the effectiveness of the proposed approach. The MOS test results show that the models with harmonic signals outperform the baseline models in both sound quality and singer similarity, which achieves significant improvement. The analysis also shows that it effectively improves the smoothness and continuity of harmonics in the generated audio.

# Contents
- [Abstract](#abstract)
- [Contents](#contents)
- [Audio Samples](#audio-samples)
  - [Clean Testset](#clean-testset)
  - [Noisy Testset](#noisy-testset)

# Audio Samples

## Clean Testset

<table align="center">
    <tr><th style="text-align:center">Source Audio</th><th style="text-align:center">Target Timbre</th><th style="text-align:center">MelGAN</th><th style="text-align:center">MelGAN-H</th><th style="text-align:center">PWG</th><th style="text-align:center">PWG-S</th><th style="text-align:center">PWG-H</th></tr>
    <tr>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/source/F001_01-04.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/target/F001_01-04.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/melgan/F001_01-04.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/melgan_h/F001_01-04.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/pwg/F001_01-04.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/pwg_s/F001_01-04.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/pwg_h/F001_01-04.wav"></audio>
        </td>
    </tr>
    <tr>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/source/F002_01-08.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/target/F002_01-08.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/melgan/F002_01-08.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/melgan_h/F002_01-08.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/pwg/F002_01-08.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/pwg_s/F002_01-08.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/pwg_h/F002_01-08.wav"></audio>
        </td>
    </tr>
    <tr>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/source/F003_01-01.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/target/F003_01-01.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/melgan/F003_01-01.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/melgan_h/F003_01-01.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/pwg/F003_01-01.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/pwg_s/F003_01-01.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/pwg_h/F003_01-01.wav"></audio>
        </td>
    </tr>
    <tr>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/source/F004_01-03.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/target/F004_01-03.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/melgan/F004_01-03.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/melgan_h/F004_01-03.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/pwg/F004_01-03.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/pwg_s/F004_01-03.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/pwg_h/F004_01-03.wav"></audio>
        </td>
    </tr>
    <tr>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/source/M001_01-04.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/target/M001_01-04.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/melgan/M001_01-04.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/melgan_h/M001_01-04.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/pwg/M001_01-04.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/pwg_s/M001_01-04.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/pwg_h/M001_01-04.wav"></audio>
        </td>
    </tr>
    <tr>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/source/M002_01-02.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/target/M002_01-02.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/melgan/M002_01-02.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/melgan_h/M002_01-02.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/pwg/M002_01-02.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/pwg_s/M002_01-02.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/pwg_h/M002_01-02.wav"></audio>
        </td>
    </tr>
    <tr>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/source/M003_01-00.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/target/M003_01-00.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/melgan/M003_01-00.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/melgan_h/M003_01-00.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/pwg/M003_01-00.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/pwg_s/M003_01-00.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/pwg_h/M003_01-00.wav"></audio>
        </td>
    </tr>
    <tr>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/source/M004_01-09.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/target/M004_01-09.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/melgan/M004_01-09.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/melgan_h/M004_01-09.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/pwg/M004_01-09.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/pwg_s/M004_01-09.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/pwg_h/M004_01-09.wav"></audio>
        </td>
    </tr>
</table>

## Noisy Testset

<table align="center">
    <tr><th style="text-align:center">Source Audio</th><th style="text-align:center">Target Timbre</th><th style="text-align:center">MelGAN</th><th style="text-align:center">MelGAN-H</th><th style="text-align:center">PWG</th><th style="text-align:center">PWG-S</th><th style="text-align:center">PWG-H</th></tr>
<tr>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/source/241_922585432_01-07.wav"></audio>       
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/target/241_922585432_01-07.wav"></audio>       
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/melgan/241_922585432_01-07.wav"></audio>       
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/melgan_h/241_922585432_01-07.wav"></audio>     
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/pwg/241_922585432_01-07.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/pwg_s/241_922585432_01-07.wav"></audio>        
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/pwg_h/241_922585432_01-07.wav"></audio>        
        </td>
    </tr>
    <tr>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/source/245_923373130_00-01.wav"></audio>       
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/target/245_923373130_00-01.wav"></audio>       
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/melgan/245_923373130_00-01.wav"></audio>       
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/melgan_h/245_923373130_00-01.wav"></audio>     
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/pwg/245_923373130_00-01.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/pwg_s/245_923373130_00-01.wav"></audio>        
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/pwg_h/245_923373130_00-01.wav"></audio>        
        </td>
    </tr>
    <tr>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/source/4_923164415_00-02.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/target/4_923164415_00-02.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/melgan/4_923164415_00-02.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/melgan_h/4_923164415_00-02.wav"></audio>       
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/pwg/4_923164415_00-02.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/pwg_s/4_923164415_00-02.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/pwg_h/4_923164415_00-02.wav"></audio>
        </td>
    </tr>
    <tr>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/source/676_922343617_00-00.wav"></audio>       
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/target/676_922343617_00-00.wav"></audio>       
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/melgan/676_922343617_00-00.wav"></audio>       
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/melgan_h/676_922343617_00-00.wav"></audio>     
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/pwg/676_922343617_00-00.wav"></audio>
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/pwg_s/676_922343617_00-00.wav"></audio>        
        </td>
        <td style="word-wrap:break-word;text-align:center">
            <audio controls style="width: 100px;text-align:center"><source src="./sample/pwg_h/676_922343617_00-00.wav"></audio>        
        </td>
    </tr>
</table>