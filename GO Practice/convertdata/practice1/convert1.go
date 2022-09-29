package main

import (
	"fmt"
	"strconv"
)

func main() {
	var str = "124"
	var num, err = strconv.Atoi(str)

	if err == nil {
		fmt.Println(num)
	}
}
