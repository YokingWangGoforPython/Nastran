proc aba_prop {} {
	global tplpath
	*creatmarkpanel comp 1 "Select comps to creat prop";
	set id_comps [hm_getmarker comps 1];
	foreach id_comps $id_comps {
		set a1 "";set a2 "";set a3 "";set a4 "";set a5 "";set a6 "";set a7 "";set a8 "";set a9 "";set a10 "";
		set name_comp [hm_getcollectorname comps $id_comp];
		regexp {(_T)([0-9])([0-9])([0-9])(_)([-0-9a-zA-Z/]+)|(_SOLID)(_)([-0-9a-zA-Z/]+)}\
		"name_comp"  a1 a2 a3 a4 a5 a6 a7 a8 a9 a10
		*creatmark props 1 $name_comp;
		set same_props [hm_getmarker props 1];
		if {$a2 == "T"} {
			set tt "$a3.$a4$a5"
			if ($same_props == []){
				*collectorcreat propeties "$name_comp" "$a7" 11
			}		
			*creatmark properties 2 "$name_comp";
			*dictionaryload properties 2 "$tplpath" "SHELLSECTION"
			*materialupdata properties 2 "$a7"
			set prop_id [hm_entityinfo id props $name_comp -byname]
			*attributeupdatadouble properties $prop_id 111 2 1 0 $tt
			*creatmark comps 2 "$name_comp";
			*propertyupdate comps 2 "$name_comp";
			} 
			elseif {$a8== "_SOLID"}{
				if {$same_props == []}{
					*collectorcreat properties "$name_comp" "$a10" 17
				}
			*dictionaryresetsolver properties "$name_comp" 1
			*creatmark properties 2 "$name_comp"
			*dictionaryload properties 2 "tplpath" "SOLIDSECTION"
			*materialupdata properties 2 "$a10";
			*creatmark comps 2 "$name_comp";
			}
		}
	}

proc nas_prop {} {
	global tplpath
	*creatmarkpanel comp 1 "Select comps to creat prop";
	set id_comps [hm_getmarker comps 1];
	foreach id_comps $id_comps {
		set a1 "";set a2 "";set a3 "";set a4 "";set a5 "";set a6 "";set a7 "";set a8 "";set a9 "";set a10 "";
		set name_comp [hm_getcollectorname comps $id_comp];
		regexp {(_T)([0-9])([0-9])([0-9])(_)([-0-9a-zA-Z/]+)|(_SOLID)(_)([-0-9a-zA-Z/]+)}\
		"name_comp"  a1 a2 a3 a4 a5 a6 a7 a8 a9 a10
		*creatmark props 1 $name_comp;
		set same_props [hm_getmarker props 1];
		if {$a2 == "T"} {
			set tt "$a3.$a4$a5"
			if ($same_props == []){
				*collectorcreat propeties "$name_comp" "$a7" 11
			}		
			*creatmark properties 2 "$name_comp";
			*dictionaryload properties 2 "$tplpath" "PSHELL"
			*materialupdata properties 2 "$a7"
			set prop_id [hm_entityinfo id props $name_comp -byname]
			*attributeupdatadouble properties $prop_id 95 1 1 0 $tt
			*creatmark comps 2 "$name_comp";
			*propertyupdate comps 2 "$name_comp";
			*creatmark properties 2 "$name_comp";
			*renumbersolverid properties 2 $id_comp 1 0 0 0 0 0
			*retainmarkerselctions 0
			} 
			elseif {$a8== "_SOLID"} {
				if {$same_props == []} {
					*collectorcreat properties "$name_comp" "$a10" 17
				}
			*dictionaryresetsolver properties "$name_comp" 1
			*creatmark properties 2 "$name_comp"
			*dictionaryload properties 2 "tplpath" "PSOLID"
			*materialupdata properties 2 "$a10";
			*creatmark comps 2 "$name_comp";
			*propertyupdate comps 2 "$name_comp"
			*renumbersolverid properties 2 $id_comp 1 0 0 0 0 0
			}
		}
	}

proc opti_prop {} {
	global tplpath
	*creatmarkpanel comp 1 "Select comps to creat prop";
	set id_comps [hm_getmarker comps 1];
	foreach id_comps $id_comps {
		set a1 "";set a2 "";set a3 "";set a4 "";set a5 "";set a6 "";set a7 "";set a8 "";set a9 "";set a10 "";
		set name_comp [hm_getcollectorname comps $id_comp];
		regexp {(_T)([0-9])([0-9])([0-9])(_)([-0-9a-zA-Z/]+)|(_SOLID)(_)([-0-9a-zA-Z/]+)}\
		"name_comp"  a1 a2 a3 a4 a5 a6 a7 a8 a9 a10
		*creatmark props 1 $name_comp;
		set same_props [hm_getmarker props 1];
		if {$a2 == "T"} {
			set tt "$a3.$a4$a5"
			if ($same_props == []){
				*collectorcreat propeties "$name_comp" "$a7" 11
			}		
			*creatmark properties 2 "$name_comp";
			*dictionaryload properties 2 "$tplpath" "PSHELL"
			*materialupdata properties 2 "$a7"
			set prop_id [hm_entityinfo id props $name_comp -byname]
			*attributeupdatadouble properties $prop_id 95 1 1 0 $tt
			*creatmark comps 2 "$name_comp";
			*propertyupdate comps 2 "$name_comp";
			*creatmark properties 2 "$name_comp";
			*renumbersolverid properties 2 $id_comp 1 0 0 0 0 0
			*retainmarkerselctions 0
			} 
			elseif {$a8== "_SOLID"} {
				if {$same_props == []} {
					*collectorcreat properties "$name_comp" "$a10" 17
				}
			*dictionaryresetsolver properties "$name_comp" 1
			*creatmark properties 2 "$name_comp"
			*dictionaryload properties 2 "tplpath" "PSOLID"
			*materialupdata properties 2 "$a10";
			*creatmark comps 2 "$name_comp";
			*propertyupdate comps 2 "$name_comp"
			*renumbersolverid properties 2 $id_comp 1 0 0 0 0 0
			}
		}
	}

	set tplpath [hm_info exporttemplate]
	set a [splite $tplpath /]
	set num [expr [llength $a]-2]
	set b [lindex $a $num]
	switch $b  {
		abaqus {aba_prop}
		nastran {nas_prop}
		optistruct {opti_prop}
	}
	*clearmark comps 1;
	*clearmark comps 2;