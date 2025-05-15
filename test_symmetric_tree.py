import unittest
# Assuming your solution file is in the same directory or accessible via PYTHONPATH
from leetcode_101_symmetric_tree import Solution # Assuming your file is named leetcode_101_symmetric_tree.py

# Definition for a binary tree node (copied from your file for test setup)
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TestSymmetricTree(unittest.TestCase):
    def setUp(self):
        """Setup method to create an instance of the Solution class."""
        self.solution = Solution()

    def test_empty_tree(self):
        """Test an empty tree, which should be symmetric."""
        self.assertTrue(self.solution.isSymmetric(None))

    def test_single_node_tree(self):
        """Test a tree with a single node, which should be symmetric."""
        root = TreeNode(1)
        self.assertTrue(self.solution.isSymmetric(root))

    def test_simple_symmetric_tree(self):
        """Test a simple symmetric tree:
                1
               / \
              2   2
             / \ / \
            3  4 4  3
        """
        root = TreeNode(1)
        root.left = TreeNode(2, TreeNode(3), TreeNode(4))
        root.right = TreeNode(2, TreeNode(4), TreeNode(3))
        self.assertTrue(self.solution.isSymmetric(root))

    def test_simple_asymmetric_tree_value_diff(self):
        """Test a simple asymmetric tree due to different values:
                1
               / \
              2   2
               \   \
                3   4
        """
        root = TreeNode(1)
        root.left = TreeNode(2, None, TreeNode(3))
        root.right = TreeNode(2, None, TreeNode(4)) # Value difference
        self.assertFalse(self.solution.isSymmetric(root))

    def test_simple_asymmetric_tree_structure_diff_1(self):
        """Test a simple symmetric tree (previously mislabeled as asymmetric):
                1
               / \
              2   2
               \   /
                3 3
        """
        root = TreeNode(1)
        root.left = TreeNode(2, None, TreeNode(3))
        root.right = TreeNode(2, TreeNode(3), None) # This structure is symmetric
        self.assertTrue(self.solution.isSymmetric(root))

    def test_simple_asymmetric_tree_structure_diff_2(self):
        """Test another simple symmetric tree (previously mislabeled as asymmetric):
                1
               / \
              2   2
             /     \
            3       3
        """
        root = TreeNode(1)
        root.left = TreeNode(2, TreeNode(3), None)
        root.right = TreeNode(2, None, TreeNode(3)) # This structure is symmetric
        self.assertTrue(self.solution.isSymmetric(root))

    def test_complex_symmetric_tree(self):
        """Test a more complex symmetric tree:
                    1
                  /   \
                 2     2
                / \   / \
               3   4 4   3
              / \ / \ / \ / \
             5  6 7  8 8  7 6  5
        """
        root = TreeNode(1)
        root.left = TreeNode(2, TreeNode(3, TreeNode(5), TreeNode(6)), TreeNode(4, TreeNode(7), TreeNode(8)))
        root.right = TreeNode(2, TreeNode(4, TreeNode(8), TreeNode(7)), TreeNode(3, TreeNode(6), TreeNode(5)))
        self.assertTrue(self.solution.isSymmetric(root))

    def test_complex_asymmetric_tree(self):
        """Test a more complex asymmetric tree:
                    1
                  /   \
                 2     2
                / \   / \
               3   4 4   3
              / \ / \ / \ / \
             5  6 7  8 8  7 6  9  <-- Asymmetry here
        """
        root = TreeNode(1)
        root.left = TreeNode(2, TreeNode(3, TreeNode(5), TreeNode(6)), TreeNode(4, TreeNode(7), TreeNode(8)))
        root.right = TreeNode(2, TreeNode(4, TreeNode(8), TreeNode(7)), TreeNode(3, TreeNode(6), TreeNode(9))) # Value 9 makes it asymmetric
        self.assertFalse(self.solution.isSymmetric(root))

    def test_asymmetric_null_children(self):
        """Test asymmetry when one side has children and other doesn't:
                1
               /
              2
        """
        root = TreeNode(1, TreeNode(2))
        self.assertFalse(self.solution.isSymmetric(root))

    def test_asymmetric_null_children_mirrored(self):
        """Test asymmetry when one side has children and other doesn't (mirrored):
                1
                 \
                  2
        """
        root = TreeNode(1, None, TreeNode(2))
        self.assertFalse(self.solution.isSymmetric(root))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
