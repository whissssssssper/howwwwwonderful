# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 08:48:31 2024

@author: student
"""

def generate_truth_table():
    # P 和 Q 的可能取值
    values = [True, False]

    # 生成真值表
    print("P\tQ\tP and Q\tP or Q\tnot(P and Q)\tnot(P or Q)\tP -> Q\tQ -> P\tP <-> Q")
    for p in values:
        for q in values:
            pandq = p and q
            porq = p or q
            not_pandq = not (pandq)
            not_porq = not (porq)
            p_implies_q = (not p) or q
            q_implies_p = (not q) or p
            p_iff_q = (p_implies_q and q_implies_p)

            print(f"{p}\t{q}\t{pandq}\t{porq}\t{not_pandq}\t\t{not_porq}\t\t{p_implies_q}\t\t{q_implies_p}\t\t{p_iff_q}")

# 生成真值表
generate_truth_table()
