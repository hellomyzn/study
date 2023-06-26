using System.Collections;
using System.Collections.Generic;
using UnityEngine.UI;
using UnityEngine;

public class UiManager : MonoBehaviour {
	public GUIStyle GUIStyle;
	public GameObject scoreManager;
	public GameObject gunManager;
	ScoreManager scoreManagerScript;
	GunManager gunManagerScript;
	float time = 90;
	
	// Use this for initialization
	void Start () {
		scoreManagerScript = scoreManager.GetComponent<ScoreManager>();
		gunManagerScript = gunManager.GetComponent<GunManager>();
	}
	
	// Update is called once per frame
	void Update () {
		time -= Time.deltaTime;
	}

	void OnGUI(){
		Rect position1 = new Rect(10,390,200,40);
		Rect position2 = new Rect(10,410,200,40);
		Rect position3 = new Rect(700,390,200,40);
		Rect position4 = new Rect(700,410,200,40);

		GUI.Label (position1,"Time : " + time.ToString("f1") + "s",GUIStyle); 
		GUI.Label (position2,"Pt : " + scoreManagerScript.score ,GUIStyle); 
		GUI.Label (position3,"BulletBox : " + gunManagerScript.bulletBox,GUIStyle); 
		GUI.Label (position4,"Bullet : " + gunManagerScript.bullet + "/30",GUIStyle); 
	}
}
