1. Pipeline flow
2. Node responsibilities
3. State object fields
4. Failure propagation logic
5. Retry policy
6. Observability points



validation
→ business
→ risk
→ investment
→ router
    ├── clarification
    └── completion

2. Biggest lessons learned honestly:

* state duplication pain
* downstream reasoning drift
* threshold gaming
* confidence instability
* routing behavior
* orchestration discipline

This reflection is VERY important.

3. Weakest architectural areas still have:

* inference semantic weakness
* confidence calibration instability
* no retry strategy
* no node timing/observability
* no state immutability discipline

I must resist myself from over-engineering too early:

* adding agents
* adding tools
* adding memory
* adding RAG
* adding LangGraph prematurely



    * failure flow
    * retry flow
    * routing flow
    * clarification flow



3. Write 5 biggest lessons learned so far

Especially:

* threshold gaming
* state duplication pain
* downstream reasoning drift
* confidence instability
* orchestration separation

That reflection will compound your learning speed massively.