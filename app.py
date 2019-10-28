from vtt_to_srt.__main__ import vtt_to_srt

config = {'vtt_path': './subtitles-en.vtt'}

print(config)
path = config['vtt_path']
vtt_to_srt(path)

from utils import translate_and_compose

input_file = path.replace('.vtt','.srt')

# Translate the subtitle into Chinese, save both English and Chinese to the output srt file
# translate_and_compose(input_file, output_file, src_lang, target_lang, encoding='UTF-8', mode='split', both=True, space=False)
translate_and_compose(input_file, input_file.replace('.srt','_cn.srt'), 'en', 'zh-CN')
# translate_and_compose(input_file, 'sample_en_cn_both.srt', 'en', 'zh-CN', encoding='UTF-8-sig')