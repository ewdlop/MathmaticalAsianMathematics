# Cangjie Type Theory with Chinese Characters

This document explains algebraic data types through the lens of Chinese character composition, implemented in Huawei's Cangjie programming language.

## Overview

Algebraic data types are fundamental constructs in type theory and functional programming. This project demonstrates how Chinese character composition naturally mirrors these mathematical concepts.

## Type Operations

### 1. Sum Type (和類型)

**Mathematical Expression**: `1 + 2 = 3`  
**Chinese Expression**: `一 + 二 = 三`

Sum types represent "either-or" choices. In type theory, a sum type `A + B` can hold either a value of type `A` or a value of type `B`.

**Example in Cangjie**:
```cangjie
enum 數字 {
    | 一    // One
    | 二    // Two
    | 三    // Three
}
```

The character `三` (three) represents the concept of combining `一` (one) and `二` (two) possibilities.

### 2. Product Type (積類型)

**Character Composition**: `一 + 二 = 王`

Product types combine multiple values together. The character `王` (king/monarch) is composed of:
- `一` - a horizontal stroke (top)
- Three horizontal strokes resembling `二` stacked

This demonstrates how components combine to create a composite structure, just like product types `A × B` hold both a value of type `A` and a value of type `B`.

**Example in Cangjie**:
```cangjie
struct CharacterComposition {
    let component1: String
    let component2: String
    let result: String
}
```

### 3. Quotient Type (商類型)

**Character**: `田` (field)

Quotient types represent equivalence classes. The character `田` is divided into four equal sections, representing how a quotient type partitions values into equivalence classes.

In type theory, a quotient type `A / ~` is formed by partitioning type `A` according to an equivalence relation `~`.

**Visual Representation**:
```
田 = ┌─┬─┐
     ├─┼─┤
     └─┴─┘
```

Each section is equivalent under rotation or reflection, demonstrating the equivalence relation.

### 4. Subtraction Type (差類型)

**Character Transformation**: `愛 - 心 = 爱`

This represents the transformation from Traditional Chinese to Simplified Chinese:
- `愛` (traditional "love") contains the radical `心` (heart)
- `爱` (simplified "love") is what remains after "removing" the heart radical

In type theory, this can be seen as a type refinement or a dependent type where we remove certain constraints or components.

**Character Breakdown**:
- Traditional: `愛` = composed parts including `心` (heart)
- Simplified: `爱` = simplified structure
- Difference: The `心` radical

## Mathematical Foundations

### Type Algebra

These operations follow algebraic laws:

1. **Sum Types**: `A + B ≅ B + A` (commutativity)
2. **Product Types**: `A × B ≅ B × A` (commutativity)
3. **Quotient Types**: `(A / ~) × (B / ≈) ≅ (A × B) / ~×≈` (product of quotients)
4. **Subtraction**: Not always well-defined in type theory, but can be viewed as type refinement

### Connection to Chinese Characters

Chinese characters (漢字) evolved through composition:
- **会意** (compound ideographs): Characters formed by combining meanings
- **形声** (phono-semantic compounds): Characters with semantic and phonetic components
- **Simplification**: Reducing components while maintaining meaning

These composition rules naturally align with algebraic type operations.

## Running the Example

If you have the Cangjie compiler installed:

```bash
cjc cangjie_types.cj -o cangjie_types
./cangjie_types
```

Expected output:
```
=== Cangjie Type Theory with Chinese Characters ===

Sum Type: 一 + 二 = 三

Product Type: 一 + 二 = 王
Components combine to form: 王

Quotient Type: 田 = four equivalent sections

Subtraction Type: 愛 - 心 = 爱
Traditional: 愛
Remove: 心
Simplified: 爱

=== End of Type Theory Examples ===
```

## References

- **Cangjie Language**: Huawei's programming language for HarmonyOS
- **Algebraic Data Types**: Fundamental concept in type theory
- **Chinese Character Composition**: 六書 (Six Categories of Chinese Characters)
- **Type Theory**: Mathematical foundation for programming languages

## Further Reading

1. Types and Programming Languages (Benjamin C. Pierce)
2. 說文解字 (Shuowen Jiezi) - Classical Chinese character etymology
3. Homotopy Type Theory
4. Chinese Character Decomposition in Unicode

## License

This educational material is provided for demonstrating type theory concepts through Chinese characters.
