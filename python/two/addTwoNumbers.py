# encoding=utf8
# 使用基本得数学方法来解决问题
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 构造新的存储得数得链表
        dummy = ListNode(0)
        p = dummy
        # 进位数值
        carry_digit = 0
        # 两个链表
        p1 = l1
        p2 = l2
        # 当两个链表存在时
        # 也就是两个相加的数字位数相等
        while p1 and p2:
            # 当前两个链表的表头数值加上预设进位数
            sum = p1.val + p2.val + carry_digit
            # 进位数
            quotient = sum // 10
            # 余数
            remainder = sum % 10
            # 为链表赋值
            p.next = ListNode(remainder)
            carry_digit = quotient
            # 移动三个链表指向下一位
            p1 = p1.next
            p2 = p2.next
            p = p.next

        # p1链表长
        while p1:
            sum = p1.val + carry_digit
            quotient = sum // 10
            remainder = sum % 10
            p.next = ListNode(remainder)
            carry_digit = quotient
            p1 = p1.next
            p = p.next

        # p2链表长
        while p2:
            sum = p2.val + carry_digit
            quotient = sum // 10
            remainder = sum % 10
            p.next = ListNode(remainder)
            carry_digit = quotient
            p2 = p2.next
            p = p.next
        if carry_digit:
            p.next = ListNode(carry_digit)

        return dummy.next