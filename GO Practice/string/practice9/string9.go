package main

import (
	"fmt"
	"strings"
)

func main() {
	var data = []string{"banana", "papaya", "tomato"}
	var str = strings.Join(data, "-")
	fmt.Println(str)
}
