# Internet Economics and Finantial Technology Coursework 2022/23

For this project, I conducted experiments on an agent-based simulation of contemporary
financial markets, called the Bristol Stock Exchange (BSE).

The trader-agent explored is called the Parameterized Response
Differential Evolution (PRDE) agent, where the strategy of an
individual trader in a market is optimised by the simplest form
of differential evolution (DE). The two parameters of DE implemented for PRDE explored in this paper are K, the number of
population of candidate strategies and F, the differential weight
used to create a new strategy to replace a worse performing one.
This paper explores how setting the parameters of differential
evolution changes the profitability of traders when run in a
market with perfect elasticity of supply and demand and in a
market with unit elasticity of supply and demand.

To examine this relationship between K and F a number of
homogeneous tests are run. In a single experiment a market is
populated by PRDE traders with identical configurations of K
and F. The performance of each experiment is compared based
on the profit per second (PPS) produced by the aggregation of
all trader profit in one market session.

Results from the homogeneous tests are presented, demonstrating the optimal value for DE to be K = 5 and F = 2.0. The
overall economic efficiency of a market populated by a PRDE
trader with these K and F values outperformed the economic
efficiency of a market with the baseline setting of K = 4 and F
= 0.8.

Two additional traders are added to BSE to extend PRDE
and the performance of each is tested in a balanced group test
with the original simple PRDE trader-agent. The extension of
PRDE proved successful, as the results from the balance groups
tests recorded higher median values of total profitability of both
PRDE trader extensions.
