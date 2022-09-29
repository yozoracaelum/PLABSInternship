package main

import "fmt"

type student struct {
	name        string
	height      float64
	age         int32
	isGraduated bool
	hobbies     []string
}

var data = student{
	name:        "Julian",
	height:      178,
	age:         21,
	isGraduated: false,
	hobbies:     []string{"Making games", "Drawing"},
}

func main() {
	fmt.Printf("%b\n", data.age)    //biner
	fmt.Printf("%c\n", 1400)        //unicode
	fmt.Printf("%c\n", 1235)        //unicode
	fmt.Printf("%d\n", data.age)    //numerik
	fmt.Printf("%e\n", data.height) // scientificnotation
	fmt.Printf("%E\n", data.height)
	fmt.Printf("%f\n", data.height) //float
	fmt.Printf("%.9f\n", data.height)
	fmt.Printf("%.2f\n", data.height)
	fmt.Printf("%.f\n", data.height)
	fmt.Printf("%e\n", 0.123123123123)
	fmt.Printf("%f\n", 0.123123123123)
	fmt.Printf("%g\n", 0.123123123123)
	fmt.Printf("%o\n", data.age)   //oktal
	fmt.Printf("%p\n", &data.name) //pointer
	fmt.Printf("%q\n", " name \\ height ")
	fmt.Printf("%s\n", data.name)        //string
	fmt.Printf("%t\n", data.isGraduated) //bool
	fmt.Printf("%T\n", data.name)        //type
	fmt.Printf("%T\n", data.age)
	fmt.Printf("%T\n", data.height)
	fmt.Printf("%T\n", data.isGraduated)
	fmt.Printf("%T\n", data.hobbies)
	fmt.Printf("%v\n", data)     //interface
	fmt.Printf("%+v\n", data)    //property
	fmt.Printf("%#v\n", data)    //formatstruct
	fmt.Printf("%x\n", data.age) //hexa
	fmt.Printf("%%\n")           //%
}
