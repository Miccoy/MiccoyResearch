import numpy as np

def bond_price(cash_flows, discount_rate):
    """
    计算债券的价格
    :param cash_flows: 债券各期的现金流
    :param discount_rate: 折现率
    :return: 债券价格
    """
    periods = np.arange(1, len(cash_flows) + 1)
    present_values = cash_flows / ((1 + discount_rate) ** periods)
    return present_values.sum()

def ytm(cash_flows, bond_price_current, initial_guess=0.05, tolerance=1e-6, max_iterations=100):
    """
    计算债券的到期收益率（YTM）
    :param cash_flows: 债券各期的现金流
    :param bond_price_current: 债券当前价格
    :param initial_guess: 初始猜测的折现率
    :param tolerance: 允许的误差范围
    :param max_iterations: 最大迭代次数
    :return: 到期收益率
    """
    rate = initial_guess
    for _ in range(max_iterations):
        price = bond_price(cash_flows, rate)
        if abs(price - bond_price_current) < tolerance:
            return rate
        # 计算导数（近似）
        delta_rate = 1e-6
        price_plus_delta = bond_price(cash_flows, rate + delta_rate)
        derivative = (price_plus_delta - price) / delta_rate
        # 牛顿 - 拉夫逊法更新
        rate = rate - (price - bond_price_current) / derivative
    raise ValueError("未能在最大迭代次数内收敛到解。")

def macaulay_duration(cash_flows, discount_rate):
    """
    计算麦考利久期
    :param cash_flows: 债券各期的现金流
    :param discount_rate: 折现率
    :return: 麦考利久期
    """
    periods = np.arange(1, len(cash_flows) + 1)
    present_values = cash_flows / ((1 + discount_rate) ** periods)
    bond_price_current = present_values.sum()
    weighted_periods = periods * present_values
    return weighted_periods.sum() / bond_price_current

# 示例数据
cash_flows = np.array([50, 50,50,50,50, 50,50,50,50,1050])  # 各期现金流，假设最后一期包含本金
bond_price_current = 800  # 债券当前价格

# 计算到期收益率
discount_rate = ytm(cash_flows, bond_price_current)
print(f"到期收益率 (YTM): {discount_rate * 100:.2f}%")

# 计算麦考利久期
duration = macaulay_duration(cash_flows, discount_rate)
print(f"麦考利久期: {duration:.2f} 期")