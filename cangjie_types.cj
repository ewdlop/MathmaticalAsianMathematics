/*
 * Cangjie Type Operations with Chinese Characters
 * Demonstrating algebraic data types through Chinese character composition
 * 
 * This file illustrates:
 * 1. Sum types (一 + 二 = 三)
 * 2. Product types (一 + 二 = 王)
 * 3. Quotient types (田)
 * 4. Subtraction types (愛 - 心 = 爱)
 */

package cangjie_types

// ===== Sum Type Example =====
// A sum type represents "either-or" choices
// Mathematical: 1 + 2 = 3
// Character: 一(one) + 二(two) = 三(three)

enum 數字 {
    | 一    // One
    | 二    // Two
    | 三    // Three
}

// Sum type: Either A or B
enum SumType<A, B> {
    | Left(A)
    | Right(B)
}

func sumExample(): Unit {
    let value1: 數字 = 數字.一
    let value2: 數字 = 數字.二
    let sum: 數字 = 數字.三
    
    // In type theory, sum types represent disjoint union
    // 一 + 二 = 三 represents combining possibilities
    println("Sum Type: 一 + 二 = 三")
}

// ===== Product Type Example =====
// Product types combine multiple values together
// Character composition: 一(horizontal) + 二(two horizontals) = 王(king)
// The strokes combine to form a new character

struct CharacterComposition {
    let component1: String
    let component2: String
    let result: String
}

func productExample(): Unit {
    // Product type: combining components
    let composition = CharacterComposition(
        component1: "一",
        component2: "二", 
        result: "王"
    )
    
    println("Product Type: 一 + 二 = 王")
    println("Components combine to form: ${composition.result}")
}

// ===== Quotient Type Example =====
// Quotient types represent equivalence classes
// 田 (field) is divided into four equal parts - representing division/quotient
// Each section is equivalent under rotation

struct QuotientField {
    let sections: Array<String>
    let character: String
}

func quotientExample(): Unit {
    let field = QuotientField(
        sections: ["口", "口", "口", "口"],
        character: "田"
    )
    
    // 田 represents a quotient type - divided into equivalent sections
    println("Quotient Type: 田 = four equivalent sections")
}

// ===== Subtraction Type Example =====
// Subtraction type: removing a component
// 愛 (love, traditional) - 心 (heart) = 爱 (love, simplified)
// Removing the heart radical from traditional to get simplified

struct CharacterSubtraction {
    let traditional: String
    let removed: String
    let simplified: String
}

func subtractionExample(): Unit {
    let subtraction = CharacterSubtraction(
        traditional: "愛",
        removed: "心",
        simplified: "爱"
    )
    
    println("Subtraction Type: 愛 - 心 = 爱")
    println("Traditional: ${subtraction.traditional}")
    println("Remove: ${subtraction.removed}")
    println("Simplified: ${subtraction.simplified}")
}

// ===== Main Function =====
func main(): Unit {
    println("=== Cangjie Type Theory with Chinese Characters ===")
    println("")
    
    sumExample()
    println("")
    
    productExample()
    println("")
    
    quotientExample()
    println("")
    
    subtractionExample()
    
    println("")
    println("=== End of Type Theory Examples ===")
}
