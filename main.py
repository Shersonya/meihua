import json
import time
import sys

# 别挂配置数据
gua_data_path = "meihua_data.json"

# 别卦数据
gua_data_map = {

}
fake_delay = 10


# 读取别卦数据
def init_gua_data(json_path):
    with open(gua_data_path, 'r', encoding='utf8') as fp:
        global gua_data_map
        gua_data_map = json.load(fp)


# 爻图标映射
yao_icon_map = {
    0: "- -",
    1: "---"
}

# 经卦名
base_gua_name_map = {
    0: "坤", 1: "震", 2: "坎", 3: "兑", 4: "艮", 5: "离", 6: "巽", 7: "乾"
}


# 数字转化为二进制数组
def base_gua_to_yao(gua, yao_length=3):
    result = []
    while gua >= 1:
        level = 0 if gua % 2 == 0 else 1
        gua //= 2
        result.append(level)
    while len(result) < yao_length:
        result.append(0)
    return result


# 二进制数组转化为数字
def base_yao_to_gua(array):
    array = array[:]
    while len(array) > 0 and array[-1] == 0:
        array.pop()
    result = 0
    for i in range(len(array)):
        if array[i] == 0:
            continue
        result += pow(2, i)

    return result


# 打印一个挂
def print_gua(gua):
    yao_list = base_gua_to_yao(gua, 6)
    up_yao_list = yao_list[0:3]
    up = base_yao_to_gua(up_yao_list)

    print(yao_icon_map[up_yao_list[2]])
    print(yao_icon_map[up_yao_list[1]] + " " + base_gua_name_map[up])
    print(yao_icon_map[up_yao_list[0]])

    print("")

    down_yao_list = yao_list[3:6]
    down = base_yao_to_gua(down_yao_list)
    print(yao_icon_map[down_yao_list[2]])
    print(yao_icon_map[down_yao_list[1]] + " " + base_gua_name_map[down])
    print(yao_icon_map[down_yao_list[0]])


def old_map_new(num):
	mapping_dict = {1: 7, 2: 3, 3: 5, 4: 1, 5: 6, 6: 2, 7: 4, 0: 0}
	return mapping_dict.get(num)

def yao_index_map(num):
	mapping_dict = {1: 3, 2: 4, 3: 5, 4: 0, 5: 1, 6: 2}
	return mapping_dict.get(num)

# 使用梅花易数
def calculate_with_plum_flower():
	# 起上卦
	#print("使用梅花易数♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️♣️")
	print("用者发财")
	#print_a_wait_animation("卜上卦：", fake_delay)
	# up_base_gua = int(round(time.time() * 1000)) % 8
	up = int(input("请输入上卦数："))
	up_base_gua = old_map_new((up % 8))
	up_yao_array = base_gua_to_yao(up_base_gua)
	print("上卦获取成功,上卦为:", base_gua_name_map[up_base_gua])
	# 起下卦
	#print_a_wait_animation("正在获取下卦：", fake_delay)
	# down_base_gua = random.randint(0, 999999999999) % 8
	down = int(input("请输入下卦数："))
	down_base_gua = old_map_new((down % 8))
	down_yao_array = base_gua_to_yao(down_base_gua)
	print("下卦获取成功,下卦为:", base_gua_name_map[down_base_gua])
	dongyao = (up + down) % 6
	print("动爻获取成功，动爻数为:", dongyao)

	# 组成卦象
	#print_a_wait_animation("正在组成本卦：", fake_delay)
	print("------------------------------------------------本卦------------------------------------------------")
	yao_list = up_yao_array + down_yao_array
	# print("yaolist:" , yao_list)
	gua = base_yao_to_gua(yao_list)
	print_gua(gua)
	# 读取本卦象信息
	gua_code = str(base_gua_name_map[up_base_gua]) + str(base_gua_name_map[down_base_gua])
	gua_data = gua_data_map[gua_code]
	print("本卦为:", gua_data['name'])
	print("辞:", gua_data['words'], "译:", gua_data['white_words'])
	print("象:", gua_data['picture'], "译:", gua_data['white_picture'])
	print("卦股及策略:", gua_data['stock_suggestion'])
	print("爻辞:", gua_data['yaoci'])

	#print_a_wait_animation("正在组成互卦：", fake_delay)
	print("------------------------------------------------互卦------------------------------------------------")
	# 读取互卦象信息
	#up_hu_yao_list = [yao_list[0], yao_list[5], yao_list[4]]
	up_hu_yao_list = [yao_list[5], yao_list[0], yao_list[1]]
	up_hu_gua = base_yao_to_gua(up_hu_yao_list)
	#down_hu_yao_list = [yao_list[1], yao_list[0], yao_list[5]]
	down_hu_yao_list = [yao_list[4], yao_list[5], yao_list[0]]
	# print("up_hu_yao_list:", up_hu_yao_list)
	# print("down_hu_yao_list:", down_hu_yao_list)
	down_hu_gua = base_yao_to_gua(down_hu_yao_list)
	hu_yao_list = up_hu_yao_list + down_hu_yao_list
	hu_gua = base_yao_to_gua(hu_yao_list)
	hu_gua_code = str(base_gua_name_map[up_hu_gua]) + str(base_gua_name_map[down_hu_gua])
	hu_gua_data = gua_data_map[hu_gua_code]
	print_gua(hu_gua)
	print("互卦为:", hu_gua_data['name'])
	print("辞:", hu_gua_data['words'], "译:", hu_gua_data['white_words'])
	print("象:", hu_gua_data['picture'], "译:", hu_gua_data['white_picture'])
	print("卦股及策略:", hu_gua_data['stock_suggestion'])
	print("爻辞:", hu_gua_data['yaoci'])

	#print_a_wait_animation("正在组成变卦：", fake_delay)
	print("------------------------------------------------变卦------------------------------------------------")
	change_index = yao_index_map(dongyao)
	change_yao_list = yao_list[:]
	change_yao_list[change_index] = 0 if change_yao_list[change_index] == 1 else 1
	up_change_yao_list = change_yao_list[0:3]
	up_change_gua = base_yao_to_gua(up_change_yao_list)
	down_change_yao_list = change_yao_list[3:6]
	down_change_gua = base_yao_to_gua(down_change_yao_list)
	# print(up_change_yao_list)
	# print(down_change_yao_list)
	change_gua = base_yao_to_gua(change_yao_list)
	print_gua(change_gua)
	change_gua_code = str(base_gua_name_map[up_change_gua]) + str(base_gua_name_map[down_change_gua])
	# print(change_gua_code)
	change_gua_data = gua_data_map[change_gua_code]
	print("变卦为:", change_gua_data['name'])
	print("辞:", change_gua_data['words'], "译:", change_gua_data['white_words'])
	print("象:", change_gua_data['picture'], "译:", change_gua_data['white_picture'])
	print("卦股及策略:", change_gua_data['stock_suggestion'])
	print("爻辞:", change_gua_data['yaoci'])

def print_a_wait_animation(tips, times):
    animation = "|/-\\"
    idx = 0
    for i in range(times):
        print(tips + animation[idx % len(animation)], animation[idx % len(animation)], animation[idx % len(animation)],
              animation[idx % len(animation)], animation[idx % len(animation)], end="\r"),
        idx += 1
        time.sleep(0.1)

init_gua_data(gua_data_path)
calculate_with_plum_flower()
input("按任意键退出")


