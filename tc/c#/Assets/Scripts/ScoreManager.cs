using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ScoreManager : MonoBehaviour {
	public int score;
	// Use this for initialization
	void Start () {
		score = 0;
	}
	
	// Update is called once per frame
	void Update () {		
	}
	public void AddScore(RaycastHit hit){
		Vector3 hitPoint = hit.point;
		Vector3 targetPoint = hit.collider.gameObject.transform.position;					
		float HeadMarkerPoint= (targetPoint - hitPoint).magnitude * 10;
		if(HeadMarkerPoint < 1.0f){
			score += 100;
		}else if (HeadMarkerPoint < 2.0f){
			score += 50;
		}else{
			score += 20;
		}
	}
}
