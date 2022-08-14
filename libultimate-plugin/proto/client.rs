use std::error::Error;
use tonic::transport::Channel;
use tonic::Request;

use libultimate::lib_ultimate_client::LibUltimateClient;
use libultimate::{ControlProps, GameStateProps};

pub mod libultimate {
    tonic::include_proto!("libultimate");
}

async fn print_features(client: &mut LibUltimateClient<Channel>) -> Result<(), Box<dyn Error>> {

    let status_request = GameStateProps {
        hz: 4,
    };
    let mut stream = client
        .get_game_state(Request::new(status_request))
        .await?
        .into_inner();

    while let Some(feature) = stream.message().await? {
        println!("NOTE = {:?}", feature);
    }

    Ok(())
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut client = LibUltimateClient::connect("http://[::1]:10000").await?;

    println!("*** SIMPLE RPC ***");
    client
        .operate_controller(Request::new(ControlProps::default()))
        .await?;
    println!("\n*** SERVER STREAMING ***");
    print_features(&mut client).await?;

    Ok(())
}
