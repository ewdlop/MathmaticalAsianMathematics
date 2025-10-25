# Data 解析延拓 (Analytic Continuation)

## 概述 (Overview)

這個專案展示了解析延拓（Analytic Continuation）的概念，特別是在數學函數如階乘和黎曼ζ函數中的應用。

This project demonstrates the concept of analytic continuation, particularly in mathematical functions such as factorial and the Riemann zeta function.

## 解析延拓是什麼？(What is Analytic Continuation?)

解析延拓是複分析中的一個核心概念，它允許我們將一個在有限區域內定義的解析函數擴展到更大的區域。

Analytic continuation is a core concept in complex analysis that allows us to extend an analytic function defined on a limited domain to a larger domain.

### 經典例子 (Classic Examples)

1. **階乘函數 (Factorial Function)**
   - 原始定義：n! 只對非負整數 n ≥ 0 有定義
   - 延拓：通過 Γ(n+1)，我們可以計算負數和非整數的「階乘」
   - 例如：(-0.5)! = Γ(0.5) = √π ≈ 1.772

2. **黎曼ζ函數 (Riemann Zeta Function)**
   - 原始定義：ζ(s) = Σ(n=1 to ∞) 1/n^s，只對 Re(s) > 1 收斂
   - 延拓：可以擴展到所有複數（除了 s=1 的極點）
   - 著名結果：ζ(-1) = -1/12，給出了 1+2+3+4+... = -1/12

## 文件說明 (Files)

### factorial_general.py

提供階乘函數的解析延拓實現，通過伽瑪函數擴展到實數域。

Provides an implementation of factorial with analytic continuation via the Gamma function, extending to real numbers.

**用法 (Usage):**
```bash
# 計算整數階乘
python factorial_general.py --x 5

# 計算非整數階乘
python factorial_general.py --x -0.5

# 高精度計算
python factorial_general.py --x -3.7 --prec 80

# 性能基準測試
python factorial_general.py --bench --x -0.5 --prec-list 30 60 120 240
```

**特性 (Features):**
- 整數 n ≥ 0：使用快速的 `math.factorial`
- 非整數：使用 mpmath 的伽瑪函數，可配置精度
- 負整數：正確處理極點並拋出錯誤
- 支持任意精度計算

### 抽樣.py (sampling.py)

展示數據採樣和解析延拓的概念，特別是黎曼ζ函數的應用。

Demonstrates data sampling and analytic continuation concepts, particularly applications of the Riemann zeta function.

**用法 (Usage):**
```bash
# 顯示所有演示
python 抽樣.py --demo all

# 只顯示 ζ 函數演示
python 抽樣.py --demo zeta

# 只顯示階乘延拓
python 抽樣.py --demo factorial

# 只顯示數據採樣
python 抽樣.py --demo sampling

# 只顯示著名的求和恆等式
python 抽樣.py --demo sum
```

**演示內容 (Demonstrations):**

1. **黎曼ζ函數 (Riemann Zeta)**
   - 計算 ζ(-1) = -1/12
   - 計算 ζ(0) = -1/2
   - 計算 ζ(2) = π²/6
   - 展示在不同區域的值

2. **著名求和恆等式 (Famous Sum Identity)**
   - 1 + 2 + 3 + 4 + ... = -1/12
   - 解釋這個結果在物理學中的應用（卡西米爾效應、弦理論）

3. **階乘延拓 (Factorial Continuation)**
   - 展示如何計算負數的「階乘」
   - 通過伽瑪函數擴展到實數域

4. **數據採樣 (Data Sampling)**
   - 在收斂區域（Re(s) > 1）採樣
   - 展示延拓到其他區域的值

### test_analytic_continuation.py

測試套件，驗證所有實現的正確性。

Test suite to verify correctness of all implementations.

**用法 (Usage):**
```bash
python test_analytic_continuation.py
```

**測試內容 (Tests):**
- 階乘函數的整數、半整數、負數測試
- 黎曼ζ函數在關鍵點的值測試
- 錯誤處理測試（極點檢測）

## 數學背景 (Mathematical Background)

### 1 + 2 + 3 + 4 + ... = -1/12 的解釋

這個看似荒謬的等式實際上是通過解析延拓得出的結果：

1. 定義黎曼ζ函數：ζ(s) = 1 + 1/2^s + 1/3^s + 1/4^s + ...（Re(s) > 1）
2. 當 s = -1 時，形式上得到：ζ(-1) = 1 + 2 + 3 + 4 + ...
3. 通過解析延拓，我們可以計算 ζ(-1) 的值
4. 結果是：ζ(-1) = -1/12

**重要說明：** 這不是普通意義上的求和！這是一種正則化（regularization）技術，在理論物理中有實際應用。

### 應用 (Applications)

1. **量子場論 (Quantum Field Theory)**
   - 卡西米爾效應的計算
   - 真空能量的正則化

2. **弦理論 (String Theory)**
   - 臨界維度的計算（D = 26）
   - 發散級數的處理

3. **數論 (Number Theory)**
   - 質數分布的研究
   - 黎曼假設

## 依賴項 (Dependencies)

```bash
pip install mpmath numpy
```

## 詩歌 (Poetry)

從 README.md 引用：

```
1 + 2 + 3 + 4 + ⋯
說是無窮，卻被 ζ(−1) 惡整成 −1⁄12；
時間在哭，空間在笑，
真空的能量還得繳稅給正則化的帝王。

n! 疊成階梯，踩上去的是發散，
跌下來的是 Borel 積分的殘影；
誰說無限不會反噬？
它只是裝傻，用解析延拓的笑聲報仇。
```

## 參考資料 (References)

- [MathOverflow: Non-integral cardinality](https://mathoverflow.net/posts/39046/revisions)
- Riemann Zeta Function and Analytic Continuation
- Gamma Function and Factorial Extension
- Ramanujan Summation and Regularization

## 作者 (Author)

ewdlop - 張益唐風格的數學探索

## 授權 (License)

本專案採用開源授權，歡迎學習和研究使用。
