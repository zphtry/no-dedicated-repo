using UnityEngine;
using UnityEngine.SceneManagement;
using System.Collections;

public class StartScript : MonoBehaviour
{
    public void Loading()
    {
        SceneManager.LoadScene("GameScene");
    }
}
