class Solution{
public:
    string simplifyPath(string path) {
        vector<string> stack;
        stringstream ss(path);
        string part;

        while(getline(ss, part, '/')) {
            if (part == "" || part == ".") {
                continue;
            }
            else if(part == "..") {
                if (!stack.empty()) {
                    stack.pop_back();
                }
            }
            else {
                stack.push_back(part);
            }
        }

        string result = "/";
        for(int i = 0; i < stack.size(); i++) {
            result += stack[i];
            if(i != stack.size() - 1) {
                result += "/";
            }
        }
        return result;
    }
};