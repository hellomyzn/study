using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Snipe : MonoBehaviour {
	bool snipeOnOff = false;
	public Camera camera;
	// Use this for initialization
	void Start () {
	}
	
	// Update is called once per frame
	void Update () {
		if(Input.GetMouseButtonDown(1)){
			if(snipeOnOff == false){
				StartSnipe();
			}
			else if(snipeOnOff == true){
				EndSnipe();
			}
		}
	}

	void StartSnipe(){
		GetComponent<Canvas>().enabled = true;
		snipeOnOff = true;
		camera.fieldOfView = 20;
	}

	void EndSnipe(){
		GetComponent<Canvas>().enabled = false;
		snipeOnOff = false;
		camera.fieldOfView = 60;
	}
}
