# #include <bits/stdc++.h>
#
# using namespace std;
#
# int main() {
#     int n;
#     cin >> n;
#     vector<int> a(n + 2), d(n + 2, INT_MAX);
#     for (int i = 1; i <= n; ++i) {
#         cin >> a[i];
#     }
#     for (int i = 1; i <= n; ++i) {
#         cin >> d[i];
#     }
#     set<int> left, current;
#     for (int i = 0; i < n + 2; ++i) {
#         left.insert(i);
#         current.insert(i);
#     }
#     for (int z = 0; z < n; ++z) {
#         set<int> del, newCurrent;
#         for (int i : current) {
#             auto it = left.find(i);
#             if (it == left.end()) {
#                 continue;
#             }
#             int _prev = *prev(it);
#             int _next = *next(it);
#             if (a[_prev] + a[_next] > d[i]) {
#                 del.insert(i);
#                 newCurrent.insert(_prev);
#                 newCurrent.insert(_next);
#             }
#         }
#         cout << del.size() << ' ';
#         for (auto it : del) {
#             left.erase(it);
#         }
#         current = newCurrent;
#     }
# }