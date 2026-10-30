#!/bin/bash
for i in {5..9}; do
	rm -R md"$((i))"
	mkdir md"$((i))"
	gmx grompp -f mdp/md.mdp -p topol.top -c unf.pdb -o md"$((i))"/md"$((i))".tpr -maxwarn 99
done
