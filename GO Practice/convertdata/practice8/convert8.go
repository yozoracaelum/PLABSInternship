package main

import (
	"fmt"
	"strconv"
)

func main() {
	var str = "true"
	var bul, err = strconv.ParseBool(str)

	if err == nil {
		fmt.Println(bul)
	}
}
