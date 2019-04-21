# TianTcl - Whisper game - generator

import random

_subject    = ["กัปตัน","เทพค้อน","ยักษ์เขียว","เกราะเหล็ก","แมงมุม","มนุษย์มด","ตาเหยี่ยว","เสือดำ"]
ext_sub     = ["ตัวจิ๋ว","นักกล้าม","คนเหล็ก","หล่อเหลา","ผู้หิวโหย"]
_verb       = ["กำลังบิน","กลิ้ง","คลาน","นอน","เต้น"]
ext_verb    = [None,"อย่างรวดเร็ว","ช้าๆ","เสียงดังมาก","อย่างรุนแรง","อย่างบ้าคลั่ง","อย่างขาดสติ"]
_object     = ["ไปสู้กับธานอส","ไปหาอินฟินิตี้สโตน","กินข้าว","เข้าห้องน้ำ"]
ext_obj     = ["ที่ดาวอังคาร","ที่บ้านเพื่อน","รังมด","ป่าใหญ่","ทุ่งหญ้า","ดาวไททัน"]

def make(_part):

    if _part == "subject":
        word = random.choice(_subject)
    elif _part == "verb":
        word = random.choice(_verb)
    elif _part == "object":
        word = random.choice(_object)
    elif _part == "ext subject":
        word = random.choice(ext_sub)
    elif _part == "ext verb":
        word = random.choice(ext_verb)
    elif _part == "ext object":
        word = random.choice(ext_obj)
    return word

def gen():
    parts =["subject","ext subject","verb","object","ext object","ext verb"]
    sentence = ""
    for part in parts:
        word = make(part)
        if word is not None:
            sentence += word
    return sentence
