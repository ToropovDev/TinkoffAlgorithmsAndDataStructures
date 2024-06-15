// Двигай!

#include <cstdio>
#include <string>
#include <random>
#include <cassert>
#include <algorithm>
#include <tuple>

using namespace std;


bool isPrime(int n) {
    for (int i = 2; i <= n / i; i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return n > 1;
}

int prevPrime(int n) {
    assert(n>=2);
    while (true) {
        n--;
        if (isPrime(n)) {
            return n;
        }
    }
}

int nextPrime(int n) {
    while (true) {
        n++;
        if (isPrime(n)) {
            return n;
        }
    }
}

struct Hash {
    int r1;
    int r2;
};

bool operator < (const Hash &left, const Hash &right) {
    return tie(left.r1, left.r2) < tie(right.r1, right.r2);
}

int main() {
    std::mt19937 gen(random_device{}());
    int m1 = prevPrime(uniform_int_distribution<int>(2000*1000*1000, 2000*1000*1000+100*1000*1000)(gen));
    int m2 = prevPrime(uniform_int_distribution<int>(2000*1000*1000, 2000*1000*1000+100*1000*1000)(gen));
    assert(m1!=m2);
    char buffer[100000+1];
    scanf("%100000s", buffer);
    string a(buffer);
    scanf("%100000s", buffer);
    string b(buffer);
    int p = nextPrime('z' - '0' + 1);
    int n = (int)max(b.size()*2, a.size());
    vector<int>pows1(1 + n);
    vector<int>pows2(1 + n);
    pows1[0] = 1 % m1;
    pows2[0] = 1 % m2;

    for (int i = 1; i <= n; i++) {
        pows1[i] = int((1LL * pows1[i - 1] * p) % m1);
        pows2[i] = int((1LL * pows2[i - 1] * p) % m2);
    }

    vector<int> bsums1(1 + b.size() * 2);
    vector<int> bsums2(1 + b.size() * 2);
    bsums1[0] = 0;
    bsums2[0] = 0;

    for (int i = 1; i <= (int)b.size()*2; i++) {
        bsums1[i] = int((bsums1[i - 1] + 1LL * b[i % b.size()] * pows1[i]) % m1);
        bsums2[i] = int((bsums2[i - 1] + 1LL * b[i % b.size()] * pows2[i]) % m2);
    }

    vector<int> asums1(1 + a.size());
    vector<int> asums2(1 + a.size());
    asums1[0] = 0;
    asums2[0] = 0;

    for (int i = 1; i <= (int)a.size(); i++) {
        asums1[i] = int((asums1[i - 1] + 1LL * a[i - 1] * pows1[i]) % m1);
        asums2[i] = int((asums2[i - 1] + 1LL * a[i - 1] * pows2[i]) % m2);
    }

    vector<Hash> shifts;
    for (int i = (int)b.size(); i < (int)b.size()*2; i++) {
        int r1 = int(((0LL + bsums1[i] - bsums1[i - (int)b.size()] + m1) * pows1[n - i]) % m1);
        int r2 = int(((0LL + bsums2[i] - bsums2[i - (int)b.size()] + m2) * pows2[n - i]) % m2);
        shifts.push_back(Hash{r1, r2});
    }

    sort(shifts.begin(), shifts.end());
    int res = 0;
    for (int i = (int)b.size(); i <= (int)a.size(); i++) {
        int r1 = int(((0LL + asums1[i] - asums1[i - (int)b.size()] + m1) * pows1[n - i]) % m1);
        int r2 = int(((0LL + asums2[i] - asums2[i - (int)b.size()] + m2) * pows2[n - i]) % m2);
        Hash hash{r1, r2};
        if (binary_search(shifts.begin(), shifts.end(), hash))
            res++;
    }
    printf("%d", res);
    return 0;
}
