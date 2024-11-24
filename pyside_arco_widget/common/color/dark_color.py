from enum import Enum

from color_base import ColorEnum


class Red(ColorEnum):
    default = (247, 105, 101)
    red_1 = (77, 0, 10)
    red_2 = (119, 6, 17)
    red_3 = (161, 22, 31)
    red_4 = (203, 46, 52)
    red_5 = (245, 78, 78)
    red_6 = (247, 105, 101)
    red_7 = (249, 141, 134)
    red_8 = (251, 176, 167)
    red_9 = (253, 209, 202)
    red_10 = (255, 240, 236)


class OrangeRed(ColorEnum):
    default = (249, 146, 90)
    orange_red_1 = (77, 14, 0)
    orange_red_2 = (119, 30, 5)
    orange_red_3 = (162, 55, 20)
    orange_red_4 = (204, 87, 41)
    orange_red_5 = (247, 126, 69)
    orange_red_6 = (249, 146, 90)
    orange_red_7 = (250, 173, 125)
    orange_red_8 = (252, 198, 161)
    orange_red_9 = (253, 222, 197)
    orange_red_10 = (255, 244, 235)


class Orange(ColorEnum):
    default = (255, 150, 38)
    orange_1 = (77, 27, 0)
    orange_2 = (121, 48, 4)
    orange_3 = (166, 75, 10)
    orange_4 = (210, 105, 19)
    orange_5 = (255, 141, 31)
    orange_6 = (255, 150, 38)
    orange_7 = (255, 179, 87)
    orange_8 = (255, 205, 135)
    orange_9 = (255, 227, 184)
    orange_10 = (255, 247, 232)


class Gold(ColorEnum):
    default = (249, 204, 68)
    gold_1 = (77, 45, 0)
    gold_2 = (119, 75, 4)
    gold_3 = (162, 111, 15)
    gold_4 = (204, 150, 31)
    gold_5 = (247, 192, 52)
    gold_6 = (249, 204, 68)
    gold_7 = (250, 220, 108)
    gold_8 = (252, 233, 149)
    gold_9 = (253, 244, 190)
    gold_10 = (255, 252, 232)


class Yellow(ColorEnum):
    default = (251, 233, 75)
    yellow_1 = (77, 56, 0)
    yellow_2 = (120, 94, 7)
    yellow_3 = (163, 134, 20)
    yellow_4 = (207, 179, 37)
    yellow_5 = (250, 225, 60)
    yellow_6 = (251, 233, 75)
    yellow_7 = (252, 243, 116)
    yellow_8 = (253, 250, 157)
    yellow_9 = (254, 254, 198)
    yellow_10 = (254, 255, 240)


class Lime(ColorEnum):
    default = (184, 226, 75)
    lime_1 = (42, 77, 0)
    lime_2 = (68, 112, 6)
    lime_3 = (98, 148, 18)
    lime_4 = (132, 183, 35)
    lime_5 = (168, 219, 57)
    lime_6 = (184, 226, 75)
    lime_7 = (203, 233, 112)
    lime_8 = (222, 241, 152)
    lime_9 = (238, 248, 194)
    lime_10 = (253, 255, 238)


class Green(ColorEnum):
    default = (39, 195, 70)
    green_1 = (0, 77, 28)
    green_2 = (4, 102, 37)
    green_3 = (10, 128, 45)
    green_4 = (18, 154, 55)
    green_5 = (29, 180, 64)
    green_6 = (39, 195, 70)
    green_7 = (80, 210, 102)
    green_8 = (126, 225, 139)
    green_9 = (178, 240, 183)
    green_10 = (235, 255, 236)


class Cyan(ColorEnum):
    default = (63, 212, 207)
    cyan_1 = (0, 66, 77)
    cyan_2 = (6, 97, 108)
    cyan_3 = (17, 131, 139)
    cyan_4 = (31, 166, 170)
    cyan_5 = (48, 201, 201)
    cyan_6 = (63, 212, 207)
    cyan_7 = (102, 223, 215)
    cyan_8 = (144, 233, 225)
    cyan_9 = (190, 244, 237)
    cyan_10 = (240, 255, 252)


class Blue(ColorEnum):
    default = (90, 170, 251)
    blue_1 = (0, 26, 77)
    blue_2 = (5, 47, 120)
    blue_3 = (19, 76, 163)
    blue_4 = (41, 113, 207)
    blue_5 = (70, 154, 250)
    blue_6 = (90, 170, 251)
    blue_7 = (125, 193, 252)
    blue_8 = (161, 213, 253)
    blue_9 = (198, 232, 254)
    blue_10 = (234, 248, 255)


class ArcoBlue(ColorEnum):
    default = (60, 126, 255)
    arco_blue_1 = (0, 13, 77)
    arco_blue_2 = (4, 27, 121)
    arco_blue_3 = (14, 50, 166)
    arco_blue_4 = (29, 77, 210)
    arco_blue_5 = (48, 111, 255)
    arco_blue_6 = (60, 126, 255)
    arco_blue_7 = (104, 159, 255)
    arco_blue_8 = (147, 190, 255)
    arco_blue_9 = (190, 218, 255)
    arco_blue_10 = (234, 244, 255)


class Purple(ColorEnum):
    default = (142, 81, 218)
    purple_1 = (22, 0, 77)
    purple_2 = (39, 6, 110)
    purple_3 = (62, 19, 143)
    purple_4 = (90, 37, 176)
    purple_5 = (123, 61, 209)
    purple_6 = (142, 81, 218)
    purple_7 = (169, 116, 227)
    purple_8 = (197, 154, 237)
    purple_9 = (223, 194, 246)
    purple_10 = (247, 237, 255)


class PinkPurple(ColorEnum):
    default = (225, 61, 219)
    pink_purple_1 = (66, 0, 77)
    pink_purple_2 = (101, 3, 112)
    pink_purple_3 = (138, 13, 147)
    pink_purple_4 = (176, 27, 182)
    pink_purple_5 = (217, 46, 217)
    pink_purple_6 = (225, 61, 219)
    pink_purple_7 = (232, 102, 223)
    pink_purple_8 = (240, 146, 230)
    pink_purple_9 = (247, 193, 240)
    pink_purple_10 = (255, 242, 253)


class Magenta(ColorEnum):
    magenta_1 = (77, 0, 52)
    magenta_2 = (119, 8, 80)
    magenta_3 = (161, 23, 108)
    magenta_4 = (203, 43, 136)
    magenta_5 = (245, 69, 166)
    magenta_6 = (247, 86, 169)
    magenta_7 = (249, 122, 184)
    magenta_8 = (251, 158, 200)
    magenta_9 = (253, 195, 219)
    magenta_10 = (255, 232, 241)


class Grey(ColorEnum):
    default = (146, 146, 147)
    grey_1 = (23, 23, 26)
    grey_2 = (46, 46, 48)
    grey_3 = (72, 72, 73)
    grey_4 = (95, 95, 96)
    grey_5 = (120, 120, 122)
    grey_6 = (146, 146, 147)
    grey_7 = (171, 171, 172)
    grey_8 = (197, 197, 197)
    grey_9 = (223, 223, 223)
    grey_10 = (246, 246, 246)


class BG(ColorEnum):
    default = (23, 23, 26)
    bg_1 = (23, 23, 26)
    bg_2 = (35, 35, 36)
    bg_3 = (42, 42, 43)
    bg_4 = (49, 49, 50)
    bg_5 = (55, 55, 57)


class Text(ColorEnum):
    default = (255, 255, 255, 178.5)
    text_1 = (255, 255, 255, 229.5)
    text_2 = (255, 255, 255, 178.5)
    text_3 = (255, 255, 255, 127.5)
    text_4 = (255, 255, 255, 76.5)

