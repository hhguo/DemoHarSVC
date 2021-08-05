---
layout: default
---

# Abstract
End-to-end neural TTS has achieved excellent performance on reading style speech synthesis. However, it’s still a challenge to build a high-quality conversational TTS due to the limitations of the corpus and modeling capability. This study aims at building a conversational TTS for a voice agent under sequence to sequence modeling framework. We firstly construct a spontaneous conversational speech corpus well designed for the voice agent with a new recording scheme ensuring both recording quality and conversational speaking style. Secondly, we propose a conversation context-aware end-to-end TTS approach which has an auxiliary encoder and a conversational context encoder to reinforce the information about the current utterance and its context in a conversation as well. Experimental results show that the proposed methods produce more natural prosody in accordance with the conversational context, with significant preference gains at both utterance-level and conversation-level. Moreover, we find that the model has the ability to express some spontaneous behaviors, like fillers and repeated words, which makes the conversational speaking style more realistic.

# Contents
- [Abstract](#abstract)
- [Audio Samples](#audio-samples)
  * [Auxiliary Encoder](#auxiliary-encoder)
    + [Dialog 1](#dialog-1)
    + [Dialog 2](#dialog-2)
    + [Complete conversations](#complete-conversations)
  * [Conversational Context Encoder](#conversational-context-encoder)
    + [Dialog 1](#dialog-1-1)
    + [Dialog 2](#dialog-2-1)
    + [Complete conversation](#complete-conversation)
  * [Spontaneous behaviors](#spontaneous-behaviors)

# Audio Samples

The below models are used in our subjective experiments:
- M1: baseline model.
- M2: M1 plus auxiliary encoder.
- M3: M2 plus conversational context encoder.

The red text parts are agent (female voice), the others are user (male voice).

## Auxiliary Encoder
> Left: M1, Right: M2

### Dialog 1

<table align="center">
    <tr><th>Transcript</th><th>Audio</th></tr>
    <tr>
        <td width="60%" style="word-wrap:break-word;">
            <font color="#FF0000">您好，有什么可以帮您？</font>
        </td>
        <td>
            <audio controls style="width: 150px;"><source src="sample/phoneme/06060000100000.wav"></audio><audio controls style="width: 150px;"><source src="sample/bert/06060000100000.wav"></audio><br>
        </td>
    </tr>
    <tr>
        <td width="60%" style="word-wrap:break-word;">
            你好。能帮我制定假期计划吗？<br>
            <font color="#FF0000">可以的。那么，您要去哪里旅行呢？</font>
        </td>
        <td>
            <audio controls style="width: 150px;"><source src="sample/phoneme/06060000100002.wav"></audio><audio controls style="width: 150px;"><source src="sample/bert/06060000100002.wav"></audio><br>
        </td>
    </tr>
    <tr>
        <td width="60%" style="word-wrap:break-word;">
            嗯，其实我还没想好，能给我点建议吗？<br>
            <font color="#FF0000">可以啊，嗯，您想去热带气候的地方，还是想去凉爽的地方？</font>
        </td>
        <td>
            <audio controls style="width: 150px;"><source src="sample/phoneme/06060000100004.wav"></audio><audio controls style="width: 150px;"><source src="sample/bert/06060000100004.wav"></audio><br>
        </td>
    </tr>
    <tr>
        <td width="60%" style="word-wrap:break-word;">
            嗯，我想去一个凉爽的地方。<br>
            <font color="#FF0000">好的，我给您一些小册子，您参考参考。</font>
        </td>
        <td>
            <audio controls style="width: 150px;"><source src="sample/phoneme/06060000100006.wav"></audio><audio controls style="width: 150px;"><source src="sample/bert/06060000100006.wav"></audio><br>
        </td>
    </tr>
    <tr>
        <td width="60%" style="word-wrap:break-word;">
            谢谢。我看看。<br>
            <font color="#FF0000">好的。另外，您这次旅行的预算多少？</font>
        </td>
        <td>
            <audio controls style="width: 150px;"><source src="sample/phoneme/06060000100008.wav"></audio><audio controls style="width: 150px;"><source src="sample/bert/06060000100008.wav"></audio><br>
        </td>
    </tr>
    <tr>
        <td width="60%" style="word-wrap:break-word;">
            我觉得每天200美元左右吧。<br>
            <font color="#FF0000">好的。那您先选择目的地，缩小范围之后，我们将很乐意为您预订。</font>
        </td>
        <td>
            <audio controls style="width: 150px;"><source src="sample/phoneme/06060000100010.wav"></audio><audio controls style="width: 150px;"><source src="sample/bert/06060000100010.wav"></audio><br>
        </td>
    </tr>
</table>

### Dialog 2

<table align="center">
    <tr><th>Transcript</th><th>Audio</th></tr>
    <tr>
        <td width="60%" style="word-wrap:break-word;">
            你好。我需要预订飞机票。<br>
            <font color="#FF0000">好的，我们可以立即预订您的行程。那，您要飞往哪个城市？</font>
        </td>
        <td>
            <audio controls style="width: 150px;"><source src="sample/phoneme/06060000200002.wav"></audio><audio controls style="width: 150px;"><source src="sample/bert/06060000200002.wav"></audio><br>
        </td>
    </tr>
    <tr>
        <td width="60%" style="word-wrap:break-word;">
            我需要飞往纽约。<br>
            <font color="#FF0000">好。您希望预定几号的票？</font>
        </td>
        <td>
            <audio controls style="width: 150px;"><source src="sample/phoneme/06060000200004.wav"></audio><audio controls style="width: 150px;"><source src="sample/bert/06060000200004.wav"></audio><br>
        </td>
    </tr>
    <tr>
        <td width="60%" style="word-wrap:break-word;">
            7月4日。<br>
            <font color="#FF0000">稍等。嗯，好。您可以从洛杉矶国际机场或伯班克机场起飞，您选哪个？</font>
        </td>
        <td>
            <audio controls style="width: 150px;"><source src="sample/phoneme/06060000200006.wav"></audio><audio controls style="width: 150px;"><source src="sample/bert/06060000200006.wav"></audio><br>
        </td>
    </tr>
    <tr>
        <td width="60%" style="word-wrap:break-word;">
            嗯，哪个便宜从哪出发吧。<br>
            <font color="#FF0000">好。您希望在一天中的哪个时间飞行？</font>
        </td>
        <td>
            <audio controls style="width: 150px;"><source src="sample/phoneme/06060000200008.wav"></audio><audio controls style="width: 150px;"><source src="sample/bert/06060000200008.wav"></audio><br>
        </td>
    </tr>
    <tr>
        <td width="60%" style="word-wrap:break-word;">
            中午吧。<br>
            <font color="#FF0000">好的，已经为您找到了廉价航班。我们已经把电子机票发到您的邮箱，请您查收。</font>
        </td>
        <td>
            <audio controls style="width: 150px;"><source src="sample/phoneme/06060000200010.wav"></audio><audio controls style="width: 150px;"><source src="sample/bert/06060000200010.wav"></audio><br>
        </td>
    </tr>
</table>

### Complete conversations

<table align="center">
    <tr>
        <td width="50%" style="word-wrap:break-word;">
            <audio controls style="width: 300px;"><source src="sample/phoneme/00002.wav"></audio>
        </td>
        <td width="50%" style="word-wrap:break-word;">
            <audio controls style="width: 300px;"><source src="sample/bert/00002.wav"></audio>
        </td>
    </tr>
</table>

## Conversational Context Encoder
> Left: M1, Right: M2

### Dialog 1

<table align="center">
    <tr><th>Transcript</th><th>Audio</th></tr>
    <tr>
        <td width="60%" style="word-wrap:break-word;">
            <font color="#FF0000">您好，有什么可以帮您？</font>
        </td>
        <td>
            <audio controls style="width: 150px;"><source src="sample/bert/06060000100000.wav"></audio><audio controls style="width: 150px;"><source src="sample/chat/06060000100000.wav"></audio><br>
        </td>
    </tr>
    <tr>
        <td width="60%" style="word-wrap:break-word;">
            你好。能帮我制定假期计划吗？<br>
            <font color="#FF0000">可以的。那么，您要去哪里旅行呢？</font>
        </td>
        <td>
            <audio controls style="width: 150px;"><source src="sample/bert/06060000100002.wav"></audio><audio controls style="width: 150px;"><source src="sample/chat/06060000100002.wav"></audio><br>
        </td>
    </tr>
    <tr>
        <td width="60%" style="word-wrap:break-word;">
            嗯，其实我还没想好，能给我点建议吗？<br>
            <font color="#FF0000">可以啊，嗯，您想去热带气候的地方，还是想去凉爽的地方？</font>
        </td>
        <td>
            <audio controls style="width: 150px;"><source src="sample/bert/06060000100004.wav"></audio><audio controls style="width: 150px;"><source src="sample/chat/06060000100004.wav"></audio><br>
        </td>
    </tr>
    <tr>
        <td width="60%" style="word-wrap:break-word;">
            嗯，我想去一个凉爽的地方。<br>
            <font color="#FF0000">好的，我给您一些小册子，您参考参考。</font>
        </td>
        <td>
            <audio controls style="width: 150px;"><source src="sample/bert/06060000100006.wav"></audio><audio controls style="width: 150px;"><source src="sample/chat/06060000100006.wav"></audio><br>
        </td>
    </tr>
    <tr>
        <td width="60%" style="word-wrap:break-word;">
            谢谢。我看看。<br>
            <font color="#FF0000">好的。另外，您这次旅行的预算多少？</font>
        </td>
        <td>
            <audio controls style="width: 150px;"><source src="sample/bert/06060000100008.wav"></audio><audio controls style="width: 150px;"><source src="sample/chat/06060000100008.wav"></audio><br>
        </td>
    </tr>
    <tr>
        <td width="60%" style="word-wrap:break-word;">
            我觉得每天200美元左右吧。<br>
            <font color="#FF0000">好的。那您先选择目的地，缩小范围之后，我们将很乐意为您预订。</font>
        </td>
        <td>
            <audio controls style="width: 150px;"><source src="sample/bert/06060000100010.wav"></audio><audio controls style="width: 150px;"><source src="sample/chat/06060000100010.wav"></audio><br>
        </td>
    </tr>
</table>

### Dialog 2

<table align="center">
    <tr><th>Transcript</th><th>Audio</th></tr>
    <tr>
        <td width="60%" style="word-wrap:break-word;">
            你好。我需要预订飞机票。<br>
            <font color="#FF0000">好的，我们可以立即预订您的行程。那，您要飞往哪个城市？</font>
        </td>
        <td>
            <audio controls style="width: 150px;"><source src="sample/bert/06060000200002.wav"></audio><audio controls style="width: 150px;"><source src="sample/chat/06060000200002.wav"></audio><br>
        </td>
    </tr>
    <tr>
        <td width="60%" style="word-wrap:break-word;">
            我需要飞往纽约。<br>
            <font color="#FF0000">好。您希望预定几号的票？</font>
        </td>
        <td>
            <audio controls style="width: 150px;"><source src="sample/bert/06060000200004.wav"></audio><audio controls style="width: 150px;"><source src="sample/chat/06060000200004.wav"></audio><br>
        </td>
    </tr>
    <tr>
        <td width="60%" style="word-wrap:break-word;">
            7月4日。<br>
            <font color="#FF0000">稍等。嗯，好。您可以从洛杉矶国际机场或伯班克机场起飞，您选哪个？</font>
        </td>
        <td>
            <audio controls style="width: 150px;"><source src="sample/bert/06060000200006.wav"></audio><audio controls style="width: 150px;"><source src="sample/chat/06060000200006.wav"></audio><br>
        </td>
    </tr>
    <tr>
        <td width="60%" style="word-wrap:break-word;">
            嗯，哪个便宜从哪出发吧。<br>
            <font color="#FF0000">好。您希望在一天中的哪个时间飞行？</font>
        </td>
        <td>
            <audio controls style="width: 150px;"><source src="sample/bert/06060000200008.wav"></audio><audio controls style="width: 150px;"><source src="sample/chat/06060000200008.wav"></audio><br>
        </td>
    </tr>
    <tr>
        <td width="60%" style="word-wrap:break-word;">
            中午吧。<br>
            <font color="#FF0000">好的，已经为您找到了廉价航班。我们已经把电子机票发到您的邮箱，请您查收。</font>
        </td>
        <td>
            <audio controls style="width: 150px;"><source src="sample/bert/06060000200010.wav"></audio><audio controls style="width: 150px;"><source src="sample/chat/06060000200010.wav"></audio><br>
        </td>
    </tr>
</table>

### Complete conversation

<table align="center">
    <tr>
        <td width="50%" style="word-wrap:break-word;">
            <audio controls style="width: 300px;"><source src="sample/bert/00001.wav"></audio>
        </td>
        <td width="50%" style="word-wrap:break-word;">
            <audio controls style="width: 300px;"><source src="sample/chat/00001.wav"></audio>
        </td>
    </tr>
</table>

## Spontaneous behaviors

<table align="center">
    <tr><th>Transcript</th><th>Audio</th></tr>
    <tr>
        <td width="60%" style="word-wrap:break-word;">
            嗯嗯，呃刚刚是我接的电话。<br>
        </td>
        <td>
            <audio controls style="width: 300px;"><source src="sample/spontaneous_behaviors/filler_0.wav"></audio><br>
        </td>
    </tr>
    <tr>
        <td width="60%" style="word-wrap:break-word;">
            呃就是说不用重新申请了，您直接到达银行就可以了明天。<br>
        </td>
        <td>
            <audio controls style="width: 300px;"><source src="sample/spontaneous_behaviors/filler_1.wav"></audio><br>
        </td>
    </tr>
    <tr>
        <td width="60%" style="word-wrap:break-word;">
            啊可以可以。<br>
        </td>
        <td>
            <audio controls style="width: 300px;"><source src="sample/spontaneous_behaviors/repeat_0.wav"></audio><br>
        </td>
    </tr>
    <tr>
        <td width="60%" style="word-wrap:break-word;">
            哎对对对。<br>
        </td>
        <td>
            <audio controls style="width: 300px;"><source src="sample/spontaneous_behaviors/repeat_1.wav"></audio><br>
        </td>
    </tr>
</table>
