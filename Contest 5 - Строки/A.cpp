// Сравнение подстрок

#include <iostream>
#include <vector>


using namespace std;

size_t m;
string s;
const long long PRIME = 1000000009;
vector<unsigned long long> primePows;
vector<unsigned long long> hashes;
vector<string> res;

unsigned long long getHash(int l, int r) {
    return hashes[r + 1] - hashes[l] * primePows[r - l + 1];
}

bool checkSubstrings(int a, int b, int c, int d) {
    return getHash(a, b) == getHash(c, d);
}


int main() {
    ios_base::sync_with_stdio(false);

    cin >> s;
    cin >> m;
    hashes.resize(s.length() + 1);
    primePows.resize(s.length() + 1);
    hashes[0] = 0;
    primePows[0] = 1;

    for (int i = 0; i < s.length(); ++i)
    {
        hashes[i + 1] = hashes[i] * PRIME + s[i];
        primePows[i + 1] = primePows[i] * PRIME;
    }

    for (int i = 0; i < m; ++i)
    {
        int a, b, c, d;
        cin >> a >> b >> c >> d;
        a--;
        b--;
        c--;
        d--;
        res.emplace_back(checkSubstrings(a, b, c, d) ? "Yes" : "No");
    }
    for (const auto & re : res){
        cout << re << endl;
    }

    return 0;
}