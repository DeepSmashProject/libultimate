use std::time::Duration;
use tokio::time;
use tokio::sync::mpsc;
use tokio_stream::wrappers::ReceiverStream;
use tonic::transport::Server;
use tonic::{Request, Response, Status};

use libultimate::lib_ultimate_server::{LibUltimate, LibUltimateServer};
use libultimate::{ControlProps, ControlResult, GameStateProps, GameState};

pub mod libultimate {
    tonic::include_proto!("libultimate");
}

#[derive(Debug)]
pub struct LibUltimateService {
}

#[tonic::async_trait]
impl LibUltimate for LibUltimateService {
    async fn operate_controller(&self, request: Request<ControlProps>) -> Result<Response<ControlResult>, Status> {
        println!("GetControlProps = {:?}", request);
        let control_result = ControlResult {
            message: String::from("ok"),
        };
        return Ok(Response::new(control_result));
    }

    type GetGameStateStream = ReceiverStream<Result<GameState, Status>>;

    async fn get_game_state(
        &self,
        request: Request<GameStateProps>,
    ) -> Result<Response<Self::GetGameStateStream>, Status> {
        let hz = request.into_inner().hz;
        println!("Fighter Status = {:?}", hz);

        let (tx, rx) = mpsc::channel(4);
        let millis = (hz * (1000/60)) as u64;
        let mut interval = time::interval(Duration::from_millis(millis));

        tokio::spawn(async move {
            loop {
                let _time = interval.tick().await;
                println!("  => send");
                let game_state = GameState {
                    message: String::from("ok"),
                };
                tx.send(Ok(game_state)).await.unwrap();
            }
        });

        Ok(Response::new(ReceiverStream::new(rx)))
    }
}

#[tokio::main]
pub async fn run_server() -> Result<(), Box<dyn std::error::Error>> {
    let addr = "0.0.0.0:10000".parse().unwrap();

    println!("LibUltimateServer listening on: {}", addr);
    let libultimate_svc = LibUltimateService {
    };
    let svc = LibUltimateServer::new(libultimate_svc);
    Server::builder().add_service(svc).serve(addr).await?;
    Ok(())
}

/*#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let addr = "0.0.0.0:10000".parse().unwrap();

    println!("LibUltimateServer listening on: {}", addr);

    let libultimate_svc = LibUltimateService {
    };

    let svc = LibUltimateServer::new(libultimate_svc);

    Server::builder().add_service(svc).serve(addr).await?;

    Ok(())
}*/
