#ifndef PRECURSORDECAY_H
#define PRECURSORDECAY_H

#include "Kernel.h"

//Forward Declarations
class PrecursorDecay;

template<>
InputParameters validParams<PrecursorDecay>();

class PrecursorDecay : public Kernel
{
public:
  PrecursorDecay(const InputParameters & parameters);

protected:
  virtual Real computeQpResidual();
  virtual Real computeQpJacobian();
  virtual Real computeQpOffDiagJacobian(unsigned int jvar);

  const MaterialProperty<std::vector<Real> > & _decay_constant;
  const MaterialProperty<std::vector<Real> > & _d_decay_constant_d_temp;
  int _precursor_group;
  unsigned int _temp_id;
};

#endif //PRECURSORDECAY_H
