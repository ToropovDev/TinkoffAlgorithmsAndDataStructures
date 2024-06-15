// Кузнечик собирает монеты

#include <iostream>
#include <map>
#include <vector>

using namespace std;

int n, k;
vector<int> arr, dp, path;

int main()
{
    cin >> n >> k;
    arr.resize(n);
    dp.resize(n);
    path.resize(n);

    for (int i = 0; i < n - 2; i++)
        cin >> arr[i + 1];

    map<int, pair<int, int>> m;
    m[0] = {1, 0};
    path[0] = -1;

    for (int i = 1; i < n; i++)
    {
        auto it = m.end();
        it--;
        dp[i] = arr[i] + it->first;
        path[i] = it->second.second;
        m[dp[i]].first++;
        m[dp[i]].second = i;

        if (i >= k)
        {
            int x = dp[i - k];
            m[x].first--;
            if (!m[x].first)
                m.erase(x);
        }
    }

    int ind = n - 1;
    vector<int> result;
    while (ind != -1)
    {
        result.push_back(ind + 1);
        ind = path[ind];
    }

    cout << dp[n - 1] << endl;
    cout << result.size() - 1 << endl;
    for (int i = result.size() - 1; i >= 0; i--)
        cout << result[i] << ' ';


    return 0;
}