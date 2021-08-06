import os


INDENT = '    '

SYSTEM_DICT = {
    'Source Audio': './sample/source',
    'Target Timbre': './sample/target',
    'MelGAN': './sample/melgan',
    'MelGAN-H': './sample/melgan_h',
    'PWG': './sample/pwg',
    'PWG-S': './sample/pwg_s',
    'PWG-H': './sample/pwg_h' 
}
CASE_LIST = [
"241_922585432_01-07.wav",
"245_923373130_00-01.wav",
"4_923164415_00-02.wav",
"676_922343617_00-00.wav",
"F001_01-04.wav",
"F002_01-08.wav",
"F003_01-01.wav",
"F004_01-03.wav",
"M001_01-04.wav",
"M002_01-02.wav",
"M003_01-00.wav",
"M004_01-09.wav",
]


def main():
    output_str = '<table align="center">\n'
    output_str += INDENT + '<tr>' + \
        ''.join(['<th style="text-align:center">{}</th>'.format(system)
                for system in SYSTEM_DICT.keys()]) + '</tr>\n'
    for case in CASE_LIST:
        output_str += INDENT + '<tr>\n'
        for system in SYSTEM_DICT.keys():
            content = '<audio controls style="width: 100px;text-align:center"><source src="{}"></audio>'.format(
                '/'.join([SYSTEM_DICT[system], case]))
            output_str += INDENT * 2 + '<td style="word-wrap:break-word;text-align:center">\n'
            output_str += INDENT * 3 + content + '\n'
            output_str += INDENT * 2 + '</td>\n'
        output_str += INDENT + '</tr>\n'
    
    output_str += '</table>\n'
    print(output_str)


if __name__ == '__main__':
    main()