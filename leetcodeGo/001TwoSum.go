package main

import "fmt"

// 题目大意 #
// 在数组中找到 2 个数之和等于给定值的数字，结果返回 2 个数字在数组中的下标。

// 解题思路 #
// 顺序扫描数组，对每一个元素，在 map 中找能组合给定值的另一半数字，
// 如果找到了，直接返回 2 个数字的下标即可。
// 如果找不到，就把这个数字存入 map 中，等待扫到“另一半”数字的时候，再取出来返回结果。
func twoSum(nums []int, target int) []int {
	
	// 数字：下标 映射
	m := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		another := target - nums[i]
		if _, ok := m[another]; ok {
			return []int{m[another], i}
		}
		m[nums[i]] = i
	}
	return nil
}

func main(){
	array1 := []int{2,1,3,5}
	fmt.Print(twoSum(array1,5))
}