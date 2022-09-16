package main

import "fmt"

type Cart struct {
	prices []float32
}

func (x Cart) show() {
	var sum float32 = 0.0
	for _, d := range x.prices {
		sum = sum + d
	}
	fmt.Println(sum)
}

func main() {
	c := Cart{}
	var n int
	var x float32
	fmt.Scanln(&n)
	cart := make([]float32, n)
	for i := 0; i < n; i++ {
		fmt.Scanln(&x)
		cart[i] = x
	}
	c.prices = cart
	c.show()
}
