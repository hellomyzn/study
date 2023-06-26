using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Target : MonoBehaviour {
	public GameObject rayControl;
	public int targetLife;
	RayControl rayControlScript;
	Animator anim;

	// Use this for initialization
	void Start () {
		rayControlScript = rayControl.GetComponent<RayControl>();
		anim = GetComponent<Animator>();
		targetLife = 5;
	}
	// Update is called once per frame
	void Update () {
		if(targetLife == 0){
			TargetDown();
		}	
	}
	void TargetDown(){
		anim.SetBool("IsDown",true);
		targetLife = 5;
		Invoke("TargetUp",10f);
	}

	void TargetUp(){
		anim.SetBool("IsDown",false);
	}
}
