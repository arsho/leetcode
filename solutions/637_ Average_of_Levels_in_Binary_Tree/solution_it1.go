func averageOfLevels(root *TreeNode) []float64 {

	var response []float64
	ln := make(map[int][]int)
	response = append(response, float64(root.Val))

	getSumFromLevel(root, 0, ln)

	for i:=0;i<len(ln) ; i++ {
		response= append(response, getAverage(ln[i]))
	}

	return response
}

func getAverage(arr []int)  float64 {
	sum:=0
	for _, value := range arr {
		sum+=value
	}
	return float64(sum)/float64(len(arr))
}

func getSumFromLevel(node *TreeNode, level int, res map[int][]int) {

	if node==nil{
		return
	}
	if node.Left!=nil{
		res[level]=append(res[level],node.Left.Val)
	}
	if node.Right !=nil{
		res[level]=append(res[level],node.Right.Val)

	}
	getSumFromLevel(node.Left, level+1, res)
	getSumFromLevel(node.Right, level+1, res)
}