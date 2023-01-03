# Todo

## Language features

- [ ] IDs with spaces in and overlapping with keyword names
  - [ ] will require a more general parser
  - [ ] 'runtime' will have to figure out which tokens are operators vs. identifiers
- [ ] Events with chance
- [ ] Distributions: triangle, normal
- [ ] Task graphs
  - [ ] Basic
  - [ ] Fixed number of resources
  - [ ] Resource requirements ('skills')
- [x] Basic unit handling (no unit mixing)
- [x] Time unit conversion (minutes, seconds)
- [x] Unit algebra (dollars/time)
- [x] Currency
  - [ ] (currency conversion?!?)
- [ ] Dates?
  - [ ] Business days?
- [ ] Min, max

## Analysis outputs

- [ ] Percentile table (10%, 50%, 90%)
- [ ] Cleaner numeric precisiion (2-3 significant digits max)
- [ ] Units in output
- [ ] Sensitivity analysis

## Error handling

- [x] Default variable values
- [ ] Only show errors for executed dag components

## Other potential ideas

- [ ] Sequential logic
- [ ] Other functions
- [ ] Function definitions

## Bugs

- [x] Notebook plugin outputs old values

## Technical thoughts

- 'analysis' results (what should we show?) should be decoupled from the display of analyses (how should we show it?)
