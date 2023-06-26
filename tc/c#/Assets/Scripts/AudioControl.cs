using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AudioControl : MonoBehaviour {
	public GameObject ak47;
	AudioClip shotSound; 
	AudioClip reloadSound;
	AudioSource audioSource;
	// Use this for initialization
	void Start () {
		shotSound = Resources.Load<AudioClip>("Audio/fire");
		reloadSound = Resources.Load<AudioClip>("Audio/reload");
		audioSource  = ak47.GetComponent<AudioSource>();	
	}
	
	// Update is called once per frame
	void Update () {		
	}

	public void GunShot(){
		audioSource.PlayOneShot(shotSound);
	}

	public void ReloadSound(){
		audioSource.PlayOneShot(reloadSound);
	}
}
