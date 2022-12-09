/**
 * The Strategy interface declares operations common to all supported versions
 * of some algorithm.
 *
 * The Context uses this interface to call the algorithm defined by Concrete
 * Strategies.
 */
#include <iostream>
#include <string>
#include <stdlib.h>
#include <algorithm>
#include <vector>

using namespace std;

class Strategy
{
public:
    virtual ~Strategy() {}
    virtual string DoAlgorithm(const vector<string> &data) const = 0;
};

/**
 * The Context defines the interface of interest to clients.
 */

class Context
{
    /**
     * @var Strategy The Context maintains a reference to one of the Strategy
     * objects. The Context does not know the concrete class of a strategy. It
     * should work with all strategies via the Strategy interface.
     */
private:
    Strategy *strategy_;
    /**
     * Usually, the Context accepts a strategy through the constructor, but also
     * provides a setter to change it at runtime.
     */
public:
    Context(Strategy *strategy = nullptr) : strategy_(strategy)
    {
    }
    ~Context()
    {
        delete this->strategy_;
    }
    /**
     * Usually, the Context allows replacing a Strategy object at runtime.
     */
    void set_strategy(Strategy *strategy)
    {
        delete this->strategy_;
        this->strategy_ = strategy;
    }
    /**
     * The Context delegates some work to the Strategy object instead of
     * implementing +multiple versions of the algorithm on its own.
     */
    void DoSomeBusinessLogic() const
    {
        // ...
        cout << "Context: Sorting data using the strategy (not sure how it'll do it)\n";
        string result = this->strategy_->DoAlgorithm(vector<string>{"a", "e", "c", "b", "d"});
        cout << result << "\n";
        // ...
    }
};

/**
 * Concrete Strategies implement the algorithm while following the base Strategy
 * interface. The interface makes them interchangeable in the Context.
 */
class ConcreteStrategyA : public Strategy
{
public:
    string DoAlgorithm(const vector<string> &data) const override
    {
        string result;
        for_each(begin(data), end(data), [&result](const string &letter) {
            result += letter;
        });
        sort(begin(result), end(result));

        return result;
    }
};
class ConcreteStrategyB : public Strategy
{
    string DoAlgorithm(const vector<string> &data) const override
    {
        string result;
        for_each(begin(data), end(data), [&result](const string &letter) {
            result += letter;
        });
        sort(begin(result), end(result));
        for (int i = 0; i < result.size() / 2; i++)
        {
            swap(result[i], result[result.size() - i - 1]);
        }

        return result;
    }
};
/**
 * The client code picks a concrete strategy and passes it to the context. The
 * client should be aware of the differences between strategies in order to make
 * the right choice.
 */

void ClientCode()
{
    Context *context = new Context(new ConcreteStrategyA);
    cout << "Client: Strategy is set to normal sorting.\n";
    context->DoSomeBusinessLogic();
    cout << "\n";
    cout << "Client: Strategy is set to reverse sorting.\n";
    context->set_strategy(new ConcreteStrategyB);
    context->DoSomeBusinessLogic();
    delete context;
}

int main()
{
    ClientCode();
    return 0;
}