from scipy.stats import norm


def standard_normal_calculator():
    while True:
        print("请选择操作：")
        print("1. 输入分位点计算累计概率")
        print("2. 输入累计概率计算分位点")
        print("3. 退出")
        choice = input("请输入选项编号：")

        if choice == '1':
            try:
                z_score = float(input("请输入分位点（z 值）："))
                cumulative_probability = norm.cdf(z_score)
                print(f"分位点 {z_score} 对应的累计概率为：{cumulative_probability:.4f}")
            except ValueError:
                print("输入无效，请输入有效的数字。")
        elif choice == '2':
            try:
                probability = float(input("请输入累计概率（0 到 1 之间）："))
                if 0 <= probability <= 1:
                    z_score = norm.ppf(probability)
                    print(f"累计概率 {probability} 对应的分位点为：{z_score:.4f}")
                else:
                    print("输入的概率必须在 0 到 1 之间。")
            except ValueError:
                print("输入无效，请输入有效的数字。")
        elif choice == '3':
            print("退出计算器。")
            break
        else:
            print("无效的选项，请输入 1、2 或 3。")


if __name__ == "__main__":
    standard_normal_calculator()
