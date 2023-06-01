#include<bits/stdc++.h>
using namespace std;
// #define int long long
#define pb push_back
#define eb emplace_back
#define m_p make_pair 
#define srt(v) sort(v.begin(),v.end())
#define rsrt(v) sort(v.rbegin(),v.rend())
#define maxi(v) *max_element((v).begin(),(v).end())
#define mini(v) *min_element((v).begin(),(v).end())
#define sum(v) accumulate((v).begin(),(v).end(),0ll)
#define rev(v) reverse((v).begin(),(v).end())
#define all(v) (v).begin(),(v).end()
#define ed '\n'
#define Ed '\n'
#define no cout<<"NO"<<ed
#define yes cout<<"YES"<<ed
int max(int a,int b) {return (a>b ? a:b);}
int min(int a,int b) {return (a<b ? a:b);}
int gcd(int a,int b) {return (b == 0 ? a : gcd(b, a % b));}
int lcm(int a,int b) {return (a / gcd(a, b)) * b;}
typedef vector<int>     vi;   typedef vector<vector<int>> vvi;
void io_file(){
    #ifndef ONLINE_JUDGE 
        freopen("Input.txt","r",stdin);
        freopen("Output.txt","w",stdout);
    #endif
}
struct Node{
    int val;
    Node *left,*right;
    Node(int data){
        val=data;
        left=right=NULL;
    }
};
bool dfs(Node *root,int value){
    if(root==NULL) return false;
    if(root->val == value) return true;
    if(dfs(root->left,value)|| dfs(root->right,value)) return true;
    return false;
}
bool dls(Node *root,int value,int level,int curr){
    if(root==NULL) return false;
    if(level<=curr) return false;
    if(dls(root->left,value,level,curr+1)) return true;
    if(root->val == value) return true;
    if(dls(root->right,value,level,curr+1)) return true;
    return false;
}
bool bfs(Node *root,int value){
    if(root == NULL) return false;
    queue<Node*> s;
    s.push(root);
    while(!s.empty()){
        int size=s.size();
        for(int i=0;i<size;i++){
            Node *curr=s.front();
            s.pop();
            if(curr->val == value)  return true;
            if(curr->left) s.push(curr->left);
            if(curr->right) s.push(curr->right);
        }
    }
    return false;
}
signed main(){
    // ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL); 
    // io_file();
    // CODE........................................................................
    struct Node *root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->left->right = new Node(5);
    root->left->right->left = new Node(8);
    cout<<"VALUE TO SEARCH :  ";
    int value;cin>>value;
    cout<<"\nTILL WHAT LEVEL TO BE SEARCHED :  ";
    int level;cin>>level;
    bool check_dfs=dfs(root,value);
    bool check_bfs=bfs(root,value);
    bool check_dls=dls(root,value,level,0);
    if(check_dfs) cout<<"FOUND in DFS "<<endl;
    else cout<<"NOT FOUND in DFS "<<endl;
    if(check_bfs) cout<<"FOUND in BFS "<<endl;
    else cout<<"NOT FOUND in BFS "<<endl;
    if(check_dls) cout<<"FOUND in DLS"<<endl;
    else cout<<"NOT FOUND in DLS"<<endl;
}