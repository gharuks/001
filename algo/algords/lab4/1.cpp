TreeNode* root;
    bool find(TreeNode* node, int k){
        if(node==NULL) return false;
        if(node->val*2!=k && find2(root, k-node->val)) return true;
        if(find(node->left, k)) return true;
        return find(node->right, k);
    }
    bool find2(TreeNode* node, int k){
        if(node==NULL) return false;
        if(node->val==k) return true;
        if(node->val<k) return find2(node->right, k);
        return find2(node->left, k);
    }
    bool findTarget(TreeNode* root, int k) {
        this->root=root;
        return find(root, k);
    }