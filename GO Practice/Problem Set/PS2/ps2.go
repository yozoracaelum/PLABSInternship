package main

import "fmt"

type Timer struct {
	value string
	id    int
}

func (x *Timer) tick() {
	x.id++
	fmt.Println(x.id)
}
func main() {
	var x int
	fmt.Scanln(&x)

	t := Timer{"timer1", 0}

	for i := 0; i < x; i++ {
		t.tick()
	}
}
