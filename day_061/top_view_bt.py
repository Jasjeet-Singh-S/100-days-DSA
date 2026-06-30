''' this is what i came up with 

class Solution:
    def topView(self, root):
        # code here
        if root==None:
            return []
        
        view = [root.data]
        
        curr_node = root
        left_level = 0
        max_left_level = 0
        
        while curr_node.left!=None or curr_node.right!=None:
            if curr_node.left!=None:
                curr_node = curr_node.left
                left_level += 1
                if left_level>max_left_level:
                    view.insert(0, curr_node.data)
                    max_left_level = left_level
                else:
                    continue
            elif curr_node.right!=None:
                curr_node = curr_node.right
                left_level -= 1
        
        curr_node = root
        right_level = 0
        max_right_level = 0
        
        while curr_node.left!=None or curr_node.right!=None:  
            if curr_node.right!=None:
                curr_node = curr_node.right
                right_level += 1
                if right_level>max_right_level:
                    view.append(curr_node.data)
                    max_right_level = right_level
                else:
                    continue
            elif curr_node.left!=None:
                curr_node = curr_node.left
                right_level -= 1
                
        return view
    
but it fails this TC

            5          (hd=0)
          /   \
         5     1       (hd=-1, hd=+1)
              / \
             3   5     (hd=0, hd=+2)
            / \   \
           10  6   8   (hd=-1, hd=+1, hd=+3)
          /
         8             (hd=-2)  ← this is the missing node

and you realise that you cant approach this problem by first going left and then right 
'''